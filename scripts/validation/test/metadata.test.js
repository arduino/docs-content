import { validateMetaData } from '../validations/metadata.js'
import { Article } from '../domain/article.js'

const contentA = 
`---
title : Getting started
difficulty: easy
unknown-property: 42
description: 'Learn how to access the IMU data and control the built-in RGB via the Arduino IoT Cloud.'
tags:
  - IoT Cloud
  - IMU
  - RGB
libraries:
  - name: Arduino LSM6DSOX
    url: https://www.arduino.cc/en/Reference/ArduinoLSM6DSOX
hardware:
  - hardware/03.nano/boards/nano-rp2040-connect
software:
  - iot-cloud
---
`;

const contentB = 
`---
title : This is a very very very very very very very very very long title.
tags:
  - IoT Cloud
description: 'Learn how to access the IMU data and control the built-in RGB via the Arduino IoT Cloud.'
author: Sebastian Romero
---
`;

const articleA = new Article();
articleA.rawData = contentA;

const articleB = new Article();
articleB.rawData = contentB;
const schemaPath = "./rules/tutorial-metadata-schema.json";

test('Tests if missing/superfluous property is detected', () => {
    const errors = validateMetaData(articleA, schemaPath);
    console.log(errors);
    expect(errors.length).toBe(2);
});


test('Tests if title lenght restriction is detected', () => {
    const errors = validateMetaData(articleB, schemaPath);
    console.log(errors);
    expect(errors.length).toBe(1);
});