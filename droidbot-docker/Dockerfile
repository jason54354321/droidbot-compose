FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
        adb \
        git \
        python3 \
        python3-pip \
        default-jdk \
        wget \
        unzip \
        androguard

#&& rm -rf /var/lib/apt/lists/*

# Droidbot
WORKDIR /root

RUN git clone https://github.com/honeynet/droidbot.git && \
        cd droidbot/ && \
        pip install -e .

# Install android-command-line-tool
RUN wget https://dl.google.com/android/repository/commandlinetools-linux-6858069_latest.zip && \
        unzip commandlinetools-linux-6858069_latest.zip -d sdk && \
        rm commandlinetools-linux-6858069_latest.zip && \
        cd sdk/cmdline-tools && \
        mkdir ~/latest && \
        mv * ~/latest && mv ~/latest .

ENV ANDROID_HOME=/root/sdk

# ENV: sdkmanager
ENV PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin

RUN yes | sdkmanager --licenses
RUN sdkmanager "platforms;android-30" "platform-tools"

# ENV PATH="$PATH:/path/to/android-sdk/tools:/path/to/android-sdk/platform-tools"

# CMD ["droidbot", "-h"]
RUN apt install -y iputils-ping

# copy adb key
COPY adbkey /root/.android/adbkey
COPY adbkey.pub /root/.android/adbkey.pub

RUN adb devices

COPY test-script.py /root/

ENTRYPOINT ["python3", "test-script.py"]

CMD ["ping", "android-emulator"]

# CMD [ "droidbot", \
# 	"-d", "android-emulator:5555", \
# 	"-a", "/apk/bitbar-sample-app.apk", \
# 	"-o", "/output", \
# 	"-is_emulator"]
