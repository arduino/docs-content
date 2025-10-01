---
title: 'FPGA HDL Basics'
description: 'Learn the basics of Field Programmable Gate Arrays (FPGA) and HDL.'
---

## Hardware Required

- [MKR Vidor 4000](https://store.arduino.cc/products/arduino-mkr-vidor-4000)

## Field Programmable Gate Arrays

Field Programmable Gate Arrays, in short [FPGAs](https://en.wikipedia.org/wiki/Field-programmable_gate_array) are a relatively old way of creating custom hardware eliminating the costs associated with silicon foundries. Unfortunately most of the complexity of chip design are still there and this is the reason why most people prefers to use off the shelf chips, often accepting their limitations, rather than take the challenge to have an optimized, efficient design with exactly the hardware they need.

As it happens with Software, where there are lots of libraries you can start from, also for FPGAs there are "libraries" called IP blocks, however these are usually quite expensive and lack a standardized "plug and play" interface which causes headaches when integrating everything in a system.
What Arduino is trying to do introducing FPGAs in its product line is to take advantage of the flexibility of programmable hardware specifically to provide an extendable set of peripherals for microcontrollers taking away most of the complexity. Of course to achieve this it's necessary to impose some limitations and define a standard way to interconnect blocks so that it can be done automatically.

The first step is defining a set of standard interfaces that must be strictly responding to a given set of rules but before diving into this it's important to define which kind of interfaces we may need.
Since we are interfacing with a microcontroller the first port we need to define is a bus to interconnect processor with peripherals. Such bus should at least exist in the controller and peripheral flavors where signals are the same but with inverted directions. For some additional details on buses and controller/peripheral architecture please check this [document](http://www.cut.ac.zw/escape/mchinyuku/1410878742.pdf).

A second interface, which is important but can't be standardized is the input/output signals that connect to the external world. Here we can't define a standard as each block will provide its own set of signals however we can just bundle a set of signals in a group which we'll call a conduit.

Finally there is a third class of interfaces which may become useful which carries streaming data. In this case we want to transfer a continuous stream of data but  also want to be able to pause the flow if the receiving block is not able to process it, hence along with data we also need some kind of flow control signals pretty much like it happens on a UART.

Since we want to standardize a bit also on readability we also want to set some coding conventions. Here of course there are many different religions which rule on spaces/tabs, notation and so on so we're picking one we like...

Talking about religion we end up talking also about languages... we prefer [(System)Verilog](https://en.wikipedia.org/wiki/SystemVerilog) over [VHDL](https://en.wikipedia.org/wiki/VHDL) and most of our IP blocks are coded with it. The reason of our choice is that Verilog in general is more similar to C and also allows very nice constructs that facilitate creating parametric blocks.

## Coding Conventions

- We use a prefix in front of every declared entity so that it identifies its type, variable name is completely upper case and multiple words are separated by underscores. In particular:

| Prefix | Description                                                                                                                                                                                                   |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| w      | Wire, for all combinatorial signals, for example wDATA. Typically defined with **wire** directive                                                                                                             |
| r      | Reg, for all sequential signals, for example rSHIFTER. Typically defined with **reg** directive                                                                                                               |
| i      | Input, for all input signals in module declaration, for example iCLK. Typically defined with **input** directive                                                                                              |
| o      | Output, for all output signals in module declaration, for example oREAD. Typically defined with **output** directive                                                                                          |
| b      | Bidirectional, for all inout signals in module declaration, for example bSDA. Typically defined with **inout** directive                                                                                      |
| p      | Parameter, for all parameters that can be used to parametrize block, for example pCHANNELS. Typically defined with **param** directive                                                                        |
| c      | Constant, for all definitions which are constant or are derived values and can't be directly used to parametrize the block. For example cCHANNEL_BITS. Typically defined with **localparam** directive |
| e      | Enumerated, for all the possible constant values used by one or more signals or registers. For example a state machine state can be defined as eSTATE. Typically defined with **enum** directive              |

- We prefer spaces over tabs! The reason is that regardless of the tab size code always looks good.

- Indentation is set to two spaces.

- Conditional statement blocks shall always have begin/end constructs even if they have a single statement in them and begin/end should be on the same line of the if/else

- Signals belonging to the same group shall share a common prefix

## Interface prototypes

### Lightweight Bus

A bus to interconnect peripherals. By convention data bus is 32 bits while address bus is variable width, based on the number of registers being exposed. A bus requires the following set of signals:

| Signal       | Direction | Direction | Width | Description                                                                                                                          |
| ------------ | --------- | --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
|              | Controller    | Peripheral     |       |                                                                                                                                      |
| ADDRESS      | O         | I         | var.  | Register address, width determines                                                                                                   |
| READ         | O         | I         | 1     | Read strobe                                                                                                                          |
| READ_DATA    | I         | O         | 32    | Data being read                                                                                                                      |
| WRITE        | O         | I         | 1     | Write strobe                                                                                                                         |
| WRITE_DATA   | O         | I         | 32    | Data to write at a given address                                                                                                     |
| BYTE_ENABLE  | O         | I         | 4     | Optional signal to flag which bytes of the 32 bit word are actually going to be written                                              |
| WAIT_REQUEST | I         | O         | 1     | Optional signal to flag the peripheral is busy. Read and write strobes will be considered valid only if this signal is not asserted. |

By convention in a write cycle ADDRESS and WRITE_DATA are latched in the same clock cycle of the WRITE strobe
By contrast, in a read cycle READ_DATA is presented by peripheral on the cycle immediately following the READ strobe, which will also indicate the ADDRESS being read.

### Pipelined Bus

A bus to interconnect complex blocks that can handle more than one command at time and responds in variable time to requests. This bus extends the Lightweight bus by adding the following signals:

This behavior is also referred as 1 clock read latency and basically means that while peripheral can still have a variable number of clocks to respond to a READ or WRITE operation using the optional WAIT_REQUEST signal, this would lock the controller preventing it to perform other operations. In a way this can be considered similar to using busy loops in programming versus delays which yield to OS in order to do multitasking.

| Signal         | Direction | Direction | Width | Description                                                                                                                                                                                                                                        |
| -------------- | --------- | --------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                | Controller    | Peripheral     |       |                                                                                                                                                                                                                                                    |
| BURST_COUNT    | O         | I         | var.  | Number of sequential operations to perform                                                                                                                                                                                                         |
| READ_DATAVALID | I         | O         | 1     | Peripheral uses this signal to flag when data is being provided to controller. Can be asserted with any delay and there is no guarantee on contiunity. A read operation with a burst size of 4 will assert 4 times READ_DATAVALID per each READ strobe |

The main advantage of this approach is that controller can communicate to the peripheral the intention of reading or writing multiple data for each transaction. Both for read and write strobes in fact the BURST_COUNT signal tells peripheral how long the transaction will be.

The controller will assert WAIT_REQUEST until it is ready to accept an operation. In case of writes, BURST_COUNT and ADDRESS are sampled only on the first strobe, after which peripheral will expect the WRITE strobe to be asserted for the number of words requested and will automatically increment address.
For read operations a single READ strobe, performed when WAIT_REQUEST is not asserted, will tell the peripheral to read BURST_COUNT words that will be returned by asserting READ_DATAVALID for the requested number of words.
After a read operation has been initiated it's up to the peripheral to accept or not more operations but in general it should be possible to have at least two concurrent operations to benefit from the Pipelined Bus.

### Streaming interface

*Coming soon*

## Structure of a (System)Verilog module

A SystemVerilog module declaration can be done in several ways but the one we mostly prefer is the form where you can use parameters so that the block inputs can be customized at compile time. This would look like:

```arduino
module COUNTER #(
pWIDTH=8
) (
input                   iCLK,
input                   iRESET,
output reg [pWIDTH-1:0] oCOUNTER
);
endmodule
```

Here we just defined the prototype of the module and defined its input/output ports, now we have to add some useful logic to it by adding some code between module header and the endmodule statement.

Since we started with a counter example let's continue with that and write some code that actually implements it:

```arduino
module COUNTER #(
pWIDTH=8
) (
input               iCLK,
input               iRESET,
output [pWIDTH-1:0] oCOUNTER
);
always @(posedge iCLK)
begin
if (iRESET) begin
oCOUNTER<=0;
end else begin
oCOUNTER<= oCOUNTER+1;
end
end
endmodule
```

The code above is pretty self explanatory... at every positive clock edge, if we see input iRESET high we reset the counter, otherwise we increment it by one... note that having a reset signal restoring our block to a known state is often useful but not always necessary.

Now... this is interesting however we did something a bit tricky... we declared oCOUNTER as output reg, which means we are saying this is not just a bunch of wires but it has memory. This way we can use the `<=` assignment which is "registered" which means that the assignment will be kept for as long as the next clock cycle.

Another way we could do this is removing the reg statement in the module declaration and define the counter as follows:

```arduino
module COUNTER #(
pWIDTH=8
) (
input               iCLK,
input               iRESET,
output [pWIDTH-1:0] oCOUNTER
);
reg [pWIDTH-1:0] rCOUNTER;
always @(posedge iCLK)
begin
if (iRESET) begin
rCOUNTER<=0;
end else begin
rCOUNTER<= rCOUNTER+1;
end
end
assign oCOUNTER=rCOUNTER;
endmodule
```

This is basically the same stuff but we defined a register, worked on it and then assigned with the "continuous" `=` assignment it to the output signal. The differsence here is that while `<=` means the signal changes only at clock edges `=` assigns the value continuously so the signal will eventually change at any time, however if we assign it as we are doing in the example to a register that changes only on clock edges the resulting signal is basically just an alias.

Interestingly assignments, like any other statement in hardware description languages are parallel, which means that their order in the code is not so much relevant as they are all executed in parallel so we could have assigned oCOUNTER to rCOUNTER also before the always block. We'll come back to this as it's not completely true that order doesn't matter...

Another interesting use of continuous assignments is the possibility to create logic equations. For example we could rewrite the counter the following way:

```arduino
module COUNTER #(
pWIDTH=8
) (
input               iCLK,
input               iRESET,
output [pWIDTH-1:0] oCOUNTER
);
reg [pWIDTH-1:0] rCOUNTER;
wire [pWIDTH-1:0] wNEXT_COUNTER;
assign wNEXT_COUNTER = rCOUNTER+1;
assign oCOUNTER = rCOUNTER;
always @(posedge iCLK)
begin
if (iRESET) begin
rCOUNTER<=0;
end else begin
rCOUNTER<= wNEXT_COUNTER;
end
end
endmodule
```

We're basically still doing the same stuff but we have done it in a way that makes it a bit more clear logically. Basically we are assigning continuously the signal wNEXT_COUNTER to the value of the rCOUNTER plus one. This means that wNEXT_COUNTER will (almost) immediately change as soon as rCOUNTER changes value however rCOUNTER will be updated only on the next positive clock edge (as it has a `<=` assignment) so the result is still that rCOUNTER changes only on clock edge.

## Parallelism and precedence

As we wrote in the previous chapter all hardware description languages have the concept of parallel statements which means that as opposed to software programming languages which execute instructions sequentially, here all instructions are executed at the same time.
For example if we write a block which has the code below we will see registers changing together at a given clock edge:

```arduino
reg [pWIDTH-1:0] rCOUNT_UP, rCOUNT_DOWN;
always @(posedge iCLK)
begin
if (iRESET) begin
rCOUNT_UP<=0;
rCOUNT_DOWN<=0;
end else begin
rCOUNT_UP<= rCOUNT_UP+1;
rCOUNT_DOWN<= rCOUNT_DOWN-1;
end
end
```

Of course if everything gets executed in parallel we need to have a way to sequentialize statements which can be done by creating a simple state machine.
A state machine is a system which generates outputs based on inputs AND its internal state.
In a sense our counter was already a state machine as we have an output (oCOUNTER) that changes based on the previous state of the machine (rCOUNTER), however let's do something more interesting and create a state machine that creates a pulse of a given length when we start it.
The machine will have three states: eST_IDLE, eST_PULSE_HIGH and eST_PULSE_LOW. In the eST_IDLE we will sample the input command and when that is received we transition to eST_PULSE_HIGH, where we will stay for the given number of clocks, which we'll parametrize with pHIGH_COUNT, then we will transition to eST_PULSE_LOW where we'll stay for pLOW_COUNT and then get back to eST_IDLE...
Let's have a look at how this turns out in code:

```arduino
module PULSE_GEN #(
pWIDTH=8,
pHIGH_COUNT=240,
pLOW_COUNT=40
) (
input       iCLK,
input       iRESET,
input       iPULSE_REQ,
output reg  oPULSE
);
reg [pWIDTH-1:0] rCOUNTER;
enum reg [1:0] {
eST_IDLE,
eST_PULSE_HIGH,
eST_PULSE_LOW
} rSTATE;
always @(posedge iCLK)
begin
if (iRESET) begin
rSTATE<=eST_IDLE;
end else begin
case (rSTATE)
eST_IDLE: begin
if (iPULSE_REQ) begin
rSTATE<= eST_PULSE_HIGH;
oPULSE<= 1;
rCOUNTER <= pHIGH_COUNT-1;
end
end
eST_PULSE_HIGH: begin
rCOUNTER<= rCOUNTER-1;
if (rCOUNTER==0) begin
rSTATE<= eST_PULSE_LOW;
oPULSE<= 0;
rCOUNTER<= pLOW_COUNT-1;
end
end
eST_PULSE_LOW: begin
rCOUNTER<= rCOUNTER-1;
if (rCOUNTER==0) begin
rSTATE<= eST_IDLE;
end
end
endcase
end
end
endmodule
```

Here we see a number of new things we need to talk about. First of all we are defining the rSTATE variable using enum. This helps in assigning the state to easily understandable values rather than hard-coded numbers and has the advantage that you can insert states easily without the need to rewrite all your state machine.

Secondly we are introducing the case/endcase block which allows us to define different behaviours depending on the state of a signal. The syntax is very similar to C so it should be familiar to most readers.
It's important to note that the statements within the various case blocks will still execute in parallel but since they are conditioned by different values of the variable being examined only one at time will be enabled.
Looking at the eST_IDLE case we see that we stay in the state forever until we sense iPULSE_REQ goes high, in which case we change state, reset the counter to the period of the high state and start outputting the pulse.

Note that since oPULSE is registered it will retain its state until it's assigned again.
In the next state things get a bit more complicated... at each clock we decrement the counter, then if counter reaches 0 we also change state, change oPULSE to 0 AND we assign rCOUNTER again.
Since the two assignments are executed in parallel we need to know what this means and lucky enough all HDL mandate that if two parallel statements are executed on the same register only the last one will be really executed so the meaning of what we just wrote is that normally we decrement the counter but when counter reaches 0 we change state and re-initialize it to pLOW_COUNT.

At this point what happens in eST_PULSE_LOW becomes pretty clear as we just decrement the counter and get back to eST_IDLE as soon as it reaches 0.
Note that when we get back to eST_IDLE rCOUNTER is decremented again so the result is that rCOUNTER will be 0xff (or -1) in eST_IDLE but we don't really care as we will reset it to the proper value when we receive iPULSE_REQ.

Although we could have reset rCOUNTER also when exiting eST_PULSE_LOW, in HDL it's always better to do only what's really necessary as anything more will consume resources and make our hardware slower. At the beginning this may seem dangerous but with some experience it will become easy to see how this can help.
This same concept applies to reset logic. Unless it is really necessary, depending on how it is implemented it can consume resources and worsen system speed so it should be used with care.

## A real world example

Now let's dive in a real world example of a simple peripheral we use in Vidor, the PWM.
What we wanted to achieve is creating a small block with multiple PWM outputs with the possibility to define the relative phase of each PWM channel.

In order to do so we need a counter and several comparators that tells us when the counter is above given values so that we can toggle the outputs. Since we also want to have the PWM frequency to be programmable we need to have the counter running at a frequency different than the base one we use for our system so that its period is exactly what we need. In order to do so we use a prescaler which basically is another counter that divides the base clock down to a lower value in a way similar to baud rate generators used in UARTs.

Now let's look at the code:

```arduino
module PWM #(
parameter pCHANNELS=16,
parameter pPRESCALER_BITS=32,
parameter pMATCH_BITS=32
)
(
input                              iCLK,
input                              iRESET,
input [$clog2(2*pCHANNELS+2)-1:0]  iADDRESS,
input [31:0]                       iWRITE_DATA,
input                              iWRITE,
output reg [pCHANNELS-1:0]         oPWM
);
// register declaration
reg [pPRESCALER_BITS-1:0] rPRESCALER_CNT;
reg [pPRESCALER_BITS-1:0] rPRESCALER_MAX;
reg [pMATCH_BITS-1:0] rPERIOD_CNT;
reg [pMATCH_BITS-1:0] rPERIOD_MAX;
reg [pMATCH_BITS-1:0] rMATCH_H [pCHANNELS-1:0];
reg [pMATCH_BITS-1:0] rMATCH_L [pCHANNELS-1:0];
reg rTICK;
integer i;
always @(posedge iCLK)
begin
// logic to interface with bus.
// register map is as follows:
// 0: prescaler value
// 1: PWM period
// even registers >=2: value at which PWM output is set high
// odd registers >=2: value at which PWM output is set low
if (iWRITE) begin
// the following statement is executed only if address is >=2. case on iADDRESS[0]
// selects if address is odd (iADDRESS[0]=1) or even (iADDRESS[0]=0)
if (iADDRESS>=2) case (iADDRESS[0])
0: rMATCH_H[iADDRESS[CLogB2(pCHANNELS):1]-1]<= iWRITE_DATA;
1: rMATCH_L[iADDRESS[CLogB2(pCHANNELS):1]-1]<= iWRITE_DATA;
endcase
else begin
// we get here if iADDRESS<2
case (iADDRESS[0])
0: rPRESCALER_MAX<=iWRITE_DATA;
1: rPERIOD_MAX<=iWRITE_DATA;
endcase
end
end
// prescaler is always incrementing
rPRESCALER_CNT<=rPRESCALER_CNT+1;
rTICK<=0;
if (rPRESCALER_CNT>= rPRESCALER_MAX) begin
// if prescaler is equal or greater than the max value
// we reset it and set the tick flag which will trigger the rest of the logic
// note that tick lasts only one clock cycle as it is reset by the rTICK<= 0 above
rPRESCALER_CNT<=0;
rTICK <=1;
end
if (rTICK) begin
// we get here each time rPRESCALER_CNT is reset. from here we increment the PWM
// counter which is then clocked at a lower frequency.
rPERIOD_CNT<=rPERIOD_CNT+1;
if (rPERIOD_CNT>=rPERIOD_MAX) begin
// and of course we reset the counter when we reach the max period.
rPERIOD_CNT<=0;
end
end
// this block implements the parallel comparators that actually generate the PWM outputs
// the for loop actually generates an array of logic that compares the counter with
// the high and low match values for each channel and set the output accordingly.
for (i=0;i<pCHANNELS;i=i+1) begin
if (rMATCH_H[i]==rPERIOD_CNT)
oPWM[i] <=1;
if (rMATCH_L[i]==rPERIOD_CNT)
oPWM[i] <=0;
end
end
endmodule
```

There are a number of new things here to learn so let's start from the module declaration. Here we are using a built in function to establish the required bit width of the address bus. The purpose is to limit the address span to the minimum required for the registers so for example if we want 10 channels we need a total of 22 addresses. Since each address bit doubles the number of addresses we can use we need a total of 5 bits which result in 32 total addresses.
In order to make this parametric we define iADDRESS width as  $clog2(2*pCHANNELS+2) and we define registers as a 2 dimensional array.

Actually there are two ways to make a multidimensional array and here we are using the "unpacked" one, which basically defines the registers as separate entities by adding indices on the left side of the register declaration. The other way, we are not using in this example is the "packed" one in which indices are both on the left side of the declaration and the result is that the 2D array can also be seen as a single big register containing the concatenation of all the registers.

Another interesting trick here is how we define the logic that handles registers. First of all we are just implementing write only registers so you won't find the iREAD and iREAD_DATA signals
Secondly we wanted to have a parametric register set where only the first two registers are always present whereas the rest are dynamically defined and handled based on the number of channels we want to implement.
In order to do so we note that in a binary number the least significant bit defines whether the number is odd or even. Since we have two registers per channel this comes handy as we can differentiate our behaviour depending on whether we are below address 2 or not.

If we are below address 2 we implement the common registers which are the prescaler count and the counter period. If we are above 2 we use the LSB to decide if we are writing the value for the high or low comparator.

## Another simple example

Another simple example we can learn something from is the quadrature encoder. While it may seem simpler than the PWM it also addresses some challenges which are not trivial.
The first issue we encounter dealing with signals from external world is that we have no guarantee they are synchronous with our internal clock so we may encounter a phenomenon called metastability which causes data in registers to be undefined and to potentially change during a clock cycle. The reason for this is that if data is changing at the input of the register while we are latching it register may get into an unstable state which may "decay" to either 1 or 0 at any time. For this reason we need to resynchronize the input signal by adding a chain of registers so that even if the first register goes metastable the following will have a stable state that can feed subsequent logic without the risk of having all the logic "contaminated" by the unstable state.

Another interesting thing we're doing here is that we are using continuous assignment to determine a strobe and a direction from the quadrature signals out of the encoder. In the code there are simple graphs showing how the waveforms look like, although in order to fully understand how the waveforms come out you have to consider that the equations use signals at different points in time. This is done by simply using the shift register used to synchronize asynchronous inputs also to delay them so tapping into a different point of the shift register we can see how signal was the clock before. In particular, if we move towards the input of the shift register we get "newer" data whereas if we move towards the end we get "older" data.
If we look at the equations we see we are using the ^ operator which is a logical exclusive or (XOR) which returns 1 if the two operands are different and 0 otherwise.

Looking at the waveforms we see that the strobe generates a pulse whenever A or B have an edge and this is done by simply xoring each signal with its delayed version.
The direction signal instead is a bit more complex but we notice that it is constantly either 0 or 1 when the strobe signal is high depending on the direction the encoder is rotating. Actually we see there are pulses on the direction signal but these are not coincident with strobes so those will be ignored.

One thing that may not look obvious at first look is that the equations are parallelly calculating the same logic for all the inputs, in fact the rRESYNC_ENCODER registers are packed bidimensional arrays arranged so that the first index identifies the tap of the shift register and the second index is the encoder channel. This means that whenever we reference rRESYNC_ENCODER with a specific index we are selecting a mono-dimensional array containing all the encoder inputs at once delayed by the amount of clocks specified by the index.
This also means that when we perform a bitwise logic operation on an array we are actually instantiating multiple parallel logic equations at the same time. Note that this can be done only because the array is "packed" as with "unpacked" arrays elements are considered separate and can't take part in equations this way and they have to be addressed singularly.

As we did for the other examples the block implements multiple inputs and does this by using a for loop that checks for the enable signal (which again is an array as wide as the number of channels) and when that is high it checks for the direction and based on that either increments or decrements the counter for that channel. This is easily done using the ? : operator (conditional expression) which works exactly like in C.

Finally the bus interface is pretty simple because the only registers we have are the read only counters and we can implement this simply by checking the read signal and assigning output data with the array of counters indexed by the address, pretty much like it was a RAM.

```arduino
module QUAD_ENCODER #(
pENCODERS=2,
pENCODER_PRECISION=32
)(
input                             iCLK,
input                             iRESET,
// AVALON PERIPHERAL INTERFACE
input  [$clog2(pENCODERS)-1:0]	  iAVL_ADDRESS,
input        	                    iAVL_READ,
output reg [31:0]                 oAVL_READ_DATA,
// ENCODER INPUTS
input [pENCODERS-1:0]             iENCODER_A,
input [pENCODERS-1:0]             iENCODER_B
);
// bidimensional arrays containing encoder input states at 4 different points in time
// the first two delay taps are used to synchronize inputs with the internal clocks
// while the other two are used to compare two points in time of those signals.
reg [3:0][pENCODERS-1:0] rRESYNC_ENCODER_A,rRESYNC_ENCODER_B;
// bidimensional arrays containing the counters for each channel
reg [pENCODERS-1:0][pENCODER_PRECISION-1:0] rSTEPS;
// encoder decrementing
// A       __----____----__
// B       ____----____----
// ENABLE  __-_-_-_-_-_-_-_
// DIR     __---_---_---_--
//
// encoder incrementing
// A       ____----____----
// B       __----____----__
// ENABLE  __-_-_-_-_-_-_-_
// DIR     ___-___-___-___-
wire [pENCODERS-1:0] wENABLE =  rRESYNC_ENCODER_A[2]^rRESYNC_ENCODER_A[3]^rRESYNC_ENCODER_B[2]^rRESYNC_ENCODER_B[3];
wire [pENCODERS-1:0] wDIRECTION = rRESYNC_ENCODER_A[2]^rRESYNC_ENCODER_B[3];
integer i;
initial rSTEPS <=0;
always @(posedge iCLK)
begin
if (iRESET) begin
rSTEPS<=0;
rRESYNC_ENCODER_A<=0;
rRESYNC_ENCODER_B<=0;
end
else begin
// implement shift registers for each channel. since arrays are packed we can treat that as a monodimensional array
// and by adding inputs at the bottom we are effectively shifting data by one bit
rRESYNC_ENCODER_A<={rRESYNC_ENCODER_A,iENCODER_A};
rRESYNC_ENCODER_B<={rRESYNC_ENCODER_B,iENCODER_B};
for (i=0;i<pENCODERS;i=i+1)
begin
// if strobe is high..
if (wENABLE[i])
// increment or decrement based on direction
rSTEPS[i] <= rSTEPS[i]+ ((wDIRECTION[i]) ? 1 : -1);
end
// if PERIPHERAL interface is being read...
if (iAVL_READ)
begin
// return the value of the counter indexed by the address
oAVL_READ_DATA<= rSTEPS[iAVL_ADDRESS];
end
end
end
endmodule
```

This is probably a great example of how elegant and concise can be hardware description for such design as we described an highly parametric design where we can change counter depth and number of channels and the code scales up accordingly generating all the related logic in a very readable way.
Of course there are different ways of doing the same thing and this one of the most concise that at the same time requires a bit more understanding of the capabilities of (system)Verilog.

*Last revision 2018/07/17 by DP & SM*