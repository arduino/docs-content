### Troubleshooting Failed SSH Connection

If the SSH connection fails, there are some common things to check out:
- Has the first setup been completed? If not, go to [First Setup](/learn/first-setup) and see the instructions. The first setup will enable SSH on the board which is required to connect.
- If the SSH connection gets stuck even though first setup has been completed, it may be a local network issue. Check that the board is connected to the same network as our computer.

### Issues with mDNS 

Some networks may block using mDNS, which allows us to use a "friendly" name (`arduino@<boardname>.local`), instead of using the actual IP address of the board. There are two ways to work around this:
1. Instead of using `arduino@<boardname>.local`, use the board's IP address directly.
2. (advanced) Edit the `/etc/hosts` on your local computer. 