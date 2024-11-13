# Droidbot Docker Compose



## Prerequisite

* `Docker`
* `kvm`


This docker compose project, due to `android-emulator` image's requirement, has to run 
with Linux environment.

### For WSL
1. Make sure your wsl runs on Window11, because `wsl nested virtualization` is required.
    > https://github.com/microsoft/WSL/issues/9201#issuecomment-1464942959
    > [WIP] Add diagram here

2. Make sure `/dev/kvm` device is existed on your wsl's device directory

    ```console
    ls /dev -l | grep -iw kvm
    # crw-rw---- 10,232 root 17 Apr 16:31 kvm
    ```

### Linux
1. Make sure `/dev/kvm` device is existed in your device directory 
    ```console
    ls /dev -l | grep -iw kvm
    # crw-rw---- 10,232 root 17 Apr 16:31 kvm
    ```

## Usage

### Test setting
1. Clone the project
    ```console
    git clone https://github.com/jason54354321/droidbot-compose.git && cd droidbot-compose
    ```
2. Place your apk to be testing into `apk/` folder

3. Set testing period per app by manually modify `test_duration` variable in `test-script.py`
    > Planing to extract into env variable, or design a general setting interfact

### Execute

5. Run the droidbot-compose
    ```
    docker compose up -d
    ```
    
6. You can monitor testing process with `docker logs droidbot-compose-droidbot-1 --follow`

7. Your testing report will be place in `output/` folder
