# Capturing raw screens

Use existing captures when they show the current app. Capture new ones only when needed, and only after the user approves the plan: which device, which build, which screens, and where the files go.

## iOS Simulator

```bash
xcrun simctl list devices                              # pick a 6.9" device, e.g. iPhone 17 Pro Max
xcrun simctl boot <UDID>
xcodebuild -scheme <App> -sdk iphonesimulator -destination "id=<UDID>" -derivedDataPath /tmp/dd build
xcrun simctl install <UDID> /tmp/dd/Build/Products/Debug-iphonesimulator/<App>.app
xcrun simctl status_bar <UDID> override --time 9:41 --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3
xcrun simctl addmedia <UDID> demo.mp4                  # demo media you may publish
xcrun simctl io <UDID> screenshot store-assets/raw/iphone/home.png
```

Navigate with real taps: the Simulator window, Appium XCUITest, or your agent's simulator tool. A 6.9″ simulator captures at 1320×2868.

## Android emulator

```bash
emulator -list-avds
emulator -avd <AVD> -no-snapshot-save &
adb install -r app-debug.apk
adb shell settings put global sysui_demo_allowed 1
adb shell am broadcast -a com.android.systemui.demo -e command clock -e hhmm 0941
adb exec-out screencap -p > store-assets/raw/android/home.png
```

Many Android captures are taller than 2:1 (for example 1280×2856). Keep the raw capture as it is and set the Play `canvas` to a ratio of 2:1 or less, such as 1080×1920. The engine fits the phone inside.

## Rules while capturing

- Use demo data you are allowed to publish: no real people, no personal data, no third-party brands on screen.
- If sign-in or a paid feature is needed, ask the user. Never invent credentials and never fake a purchase.
- Save raw captures in their own folder and record how they were made in a `manifest.json`. Never edit them afterwards.
