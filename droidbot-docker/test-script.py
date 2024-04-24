import subprocess
import time
import os

# waiting for emulator
# TODO: notify instead of waiting

device_serial = 'android-emulator:5555'
apps_directory = '/apk'
output_directory = '/output'
test_duration = 600



# polling, connect to emulator
while 1:
    print("***Trying to connect adb***")
    result = subprocess.run(
        ["adb", "connect", device_serial],
        capture_output = True,
        text = True
    )

    if result.stdout:
        print("stdout:", result.stdout)
    if result.stderr:
        print("stderr:", result.stderr)

    if "already connected" in result.stdout:
        print("-------------------")
        print("***ADB connected***")
        print("-------------------")
        break
    time.sleep(3)

# polling, wait until emulator is ready
while 1:
    print("***Waiting device to come online***")
    result = subprocess.run(
        ["adb", "devices"],
        capture_output = True,
        text = True
    )

    if result.stdout:
        print("stdout:", result.stdout)
    if result.stderr:
        print("stderr:", result.stderr)

    if "5555\tdevice" in result.stdout.replace('\n', ' '):
        print("--------------------")
        print("***Device Onlined***")
        print("--------------------")
        break
    time.sleep(3)

apps = []
# get to-test-app's name
for file in os.listdir(apps_directory):
    if file.endswith(".apk"):
        apps.append(file)

for app in apps:
    app_path = os.path.join(apps_directory, app)
    print('app_path: ', app_path)

    # create output directory
    app_path_output = os.path.join(output_directory, app)
    print('output_directory: ', app_path_output)
    os.makedirs(app_path_output, exist_ok=True)

    droidbot_cmd = ['droidbot', '-d', device_serial, '-a', app_path, '-o', app_path_output, '-is_emulator']

    print('------------------------------')
    print('***Droidbot Testing Started***')
    print('------------------------------')
    subprocess.run(droidbot_cmd)

    time.sleep(test_duration)
