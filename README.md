# Droidbot Docker Compose

## Prerequisite


This docker compose project, due to `android-emulator` image's requirement, has to run 
with Linux environment.

### For WSL
1. Make sure your wsl runs on Window11, because `wsl nested virtualization` is required.

2. Make sure `/dev/kvm` device is existed on your wsl machine

    ```console
    ls /dev -l | grep -iw kvm
    # crw-rw---- 10,232 root 17 Apr 16:31 kvm
    ```

### Linux
1. Just Make sure `/dev/kvm` device is existed on your wsl machine
    ```console
    ls /dev -l | grep -iw kvm
    # crw-rw---- 10,232 root 17 Apr 16:31 kvm
    ```
[WIP]

