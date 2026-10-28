---
title: Lock a Device to Your Account
description: Use the Lock to this account setting to keep a board tied to your Arduino Cloud account, or unlock it so someone else can set it up.
tags: [Arduino Cloud, Devices, Provisioning, Education, Business]
author: Karl Söderby & Arduino Team
---

When you set up a physical board in Arduino® Cloud, the board is linked to the account that provisioned it. The **Lock to this account** setting on the device's page controls whether that link is permanent:

- **Locked**: The board stays tied to your account. Nobody else can set it up on their own account, even after you delete the device.
- **Unlocked**: The board can be handed over. Once you delete it from your account, another person can set it up under their own account.

Each type of space gets a different default when a device is first set up. You can change the setting at any time from the device's page.

<Alert type="warning">

Needs verification: the **Lock to this account** setting wasn't verified on a live device page this pass, because the test account only had a manually configured device, which doesn't show the setting. Confirm the exact position of the setting on a physical board's device page before publishing.

</Alert>

## How the Lock Works

| Setting | What Happens | Use It When |
|---|---|---|
| **On** (locked) | The physical board is permanently tied to the current account. Nobody else can set it up on another account. | The board belongs to one person or project, and you want to prevent it from being claimed by someone else, accidentally or not. |
| **Off** (unlocked) | The board isn't tied to the account once it's deleted, so a different person can set it up on their own account. | The board is shared equipment that moves between people, such as a classroom kit or a lab board. |

The lock only matters when the device changes owner. While the device is in your account, it works the same way whether it's locked or not.

## Default Lock State by Space Type

You can change the lock on any plan. The plan only decides the **default** when a device is first set up, based on the type of space the device belongs to:

| Space Type | Plans | Default | Why |
|---|---|---|---|
| **Private space** | Individual users, no organization | Unlocked | Personal boards are often reused, given away, or moved to another account. |
| **Education space** | School and education plans | Unlocked | Classroom boards are shared and handed from one student to the next. |
| **Business space** | Team and Enterprise plans | Locked | Boards are usually assigned to one employee and project. Locking them by default stops a colleague from claiming a device that isn't theirs, or disrupting an ongoing project by re-provisioning it. |

Devices that were set up before this setting was introduced were given the default for the type of space they belong to.

## Changing the Lock Setting

The owner of a device can lock or unlock it at any time:

1. Open **Devices** in the left navigation (`/devices`).
2. Select the device to open its detail page.
3. Find the **Lock to this account** setting.
4. Turn it **on** to lock the device to your account, or **off** to unlock it.

You can lock a device that started out unlocked, or unlock one that started out locked.

## Handing a Device Over to Someone Else

To give a board to someone else, for example to the next student in a class or a colleague who takes over a project, free it from your account first:

1. Open the device's detail page and turn **Lock to this account** **off**.
2. Delete the device from your account.
3. The new owner sets the board up in their own account or space, as with any new board (for example, see [Add a Wi-Fi® Board](/arduino-cloud/devices/add-wifi-board)).

<Alert type="warning">

Turn the lock off **before** you delete the device. If you delete a locked device, the board stays tied to your account and the new owner can't set it up.

</Alert>

### Reusing Boards in a Classroom

In an Education space, boards are unlocked by default, so a teacher or student can free a board at the end of a term by deleting it, and the next student can set it up straight away. If a student has set up a board in their own personal space instead of the school's space, the board is still unlocked by default in that private space. The student can delete it from their account to make it available again.

To keep a specific board reserved for one person, for example a teacher's demo board, turn its lock on.

### Protecting Boards in a Business Space

In a Business space, boards are locked by default, so ownership stays with whoever provisioned the board. To reassign a board to another person or project on purpose, its owner turns the lock off and deletes it, and then the new owner sets it up.

## Lock State From the CLI and API

The lock is also exposed to [arduino-cloud-cli](/arduino-cloud/apis-cli/cli-devices) and the [REST API](/arduino-cloud/apis-cli/rest-api-sdks), for scripted setups:

- **arduino-cloud-cli 0.8.0 or later**: Set the lock when provisioning a board with `--locked true` or `--locked false`. If you leave the flag out, the board gets the default lock state for its space. `device show` includes a **Locked** column.

  ```bash
  arduino-cloud-cli device create --name <deviceName> --port <port> --fqbn <deviceFqbn> --locked false
  arduino-cloud-cli device show --id <deviceID>
  ```

  The CLI only accepts `--locked` for boards that use [Provisioning 2.0](/arduino-cloud/devices/network-configuration#provisioning-10-vs-20). For Provisioning 1.0 boards, it fails with "locked flag is not supported for the device".

- **REST API**: Device objects include a `locked` boolean, described as "True if the device is locked and can't be claimed by another user".

## Next Steps

- [Devices Overview](/arduino-cloud/devices/devices-overview)
- [Network Configuration](/arduino-cloud/devices/network-configuration)
- [Spaces](/arduino-cloud/spaces-plans-account/spaces)
- [Arduino Cloud for Education](/arduino-cloud/education/arduino-cloud-for-education)
