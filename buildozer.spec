[app]

# (str) Title of your application
title = Amigo

# (str) Package name
package.name = amigo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py file is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application version
version = 1.0

# (int) Build version code (used for versionCode in Android)
version.code = 1

# (str) Custom source folders for requirements (deprecated. Use source roots instead)
source.include_patterns = ../../kivy/*

# (list) Application requirements
requirements = kivy, pyttsx3, wikipedia, speechrecognition, smtplib, webbrowser, pyautogui, psutil, pyjokes, pyyaml, gTTS, pyaudio, requests, google-api-python-client

# (str) URL for the application
presplash.url =

# (str) Custom source folders for requirements (deprecated. Use source roots instead)
source.include_patterns = ../../kivy/*

# (list) Application requirements
requirements = kivy, pyttsx3, wikipedia, SpeechRecognition, smtplib, webbrowser, pyautogui, psutil, pyjokes, PyYAML, gTTS, pyaudio, requests, google-api-python-client

# (str) URL for the application
presplash.url =

# (str) URL for presplash image
# presplash.image = %(source.dir)/data/presplash.png

# (str) Local path or remote url of the image to be used for presplash
presplash.source = %(source.dir)/data/presplash.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE

[python]

# (list) List of source files
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) List of directories to include (if adding directory path to the filename)
source.include_dirs = %(source.dir)/, %(source.dir)/kivy/

# (list) List of additional files and their destination (if adding directory path to the filename)
# source tree to send as additional files
source.directory = .

# (list) List of inclusions using pattern matching
source.include_patterns = ../../kivy/*

# (list) List of exclusions using pattern matching
# source.exclude_patterns = assets/*, images/*.jpg

# (str) Root of where to put all the custom .py files
# source.root = ../../my_source/

# (str) Prefixes to be stripped
source.strip = True

# (list) List of framework imports (include all your modules you do not control)
# whether they are in pypi or not
requirements = kivy, pyttsx3, wikipedia, speechrecognition, smtplib, webbrowser, pyautogui, psutil, pyjokes, pyyaml, gTTS, pyaudio, requests, google-api-python-client

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Directory to save your app
# bin_dir = ./bin

#    android
# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (int) Android API to use for minification
android.minapi.minify = 21

# (str) Android NDK version to use
android.ndk = 22.1.7171670

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android arch (one of armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = armeabi-v7a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default, light, or dark
android.app_theme = light

# (list) Pattern to whitelist for the whole project
whitelist =

# (list) Pattern to blacklist for the whole project
blacklist =

# (list) List of Java .jar files to add to the libs directory
android.add_jars = jars/kivy-garden/garden.jar,jars/libs/android/*.jar

# (list) List of Java .jar files to add to the java build
android.add_jars_to_build = jars/kivy-garden/garden.jar

# (str) Android Gradle dependencies
android.gradle_dependencies = 'com.google.guava:guava:27.1-android'

# (list) Android AAR dependencies
android.gradle_aars = androidx-collection, androidx-media, androidx-annotation

# (bool) Android package build (gradle)
android.use_kivy_gradle = 1

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk = /content/android-sdk

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk = /content/android-ndk

# (str) iOS SDK directory (if empty, it will be automatically downloaded)
ios.sdk = /content/ios-sdk

# (str) Android NDK version to use
ios.ndk = 22.1.7171670

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
ios.ndk_path = /content/android-ndk

# (str) iOS SDK directory (if empty, it will be automatically downloaded)
ios.sdk_path = /content/ios-sdk

# (bool) Use Kivy-provided [android] default build.gradle
android.gradle = 1

# (str) Title of the application
title = Amigo

# (str) Package name
package.name = amigo

# (str) Application version
package.version = 1.0

# (int) Version code - increment to update your application
package.code = 1

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Presplash background color (for Android)
android.presplash_color = #00796B

# (str) Presplash image to use
android.presplash_path = %(source.dir)/data/presplash.png

# (str) Presplash compression (use jpg for .jpg, and png for .png)
android.presplash_compression = auto

# (str) Presplash image to use for iOS
ios.presplash_path = %(source.dir)/data/presplash.png

# (str) Presplash compression (use jpg for .jpg, and png for .png)
ios.presplash_compression = auto

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,WRITE_EXTERNAL_STORAGE

# (str) Services to add to the manifest
android.services = SpeechRecognition,SpeechRecognitionKaldi

# (list) Android specific options
android.meta_data = 

# (str) iOS bundle identifier
ios.bundleid = org.test.amigo

# (str) iOS app store URL
ios.app_store = 

# (list) iOS services to add to the project
ios.services = 

# (str) iPad bundle identifier
ios.ipad_bundleid = org.test.amigo

# (str) URL for an image to use as an app icon
ios.icon_path = %(source.dir)/data/icon.png

# (str) iOS launch image
ios.ios_launch_image = %(source.dir)/data/launch.png

# (str) iOS launch background image
ios.ios_background_image = %(source.dir)/data/background.png

# (str) Splash image for iPad
ios.splash_path = %(source.dir)/data/splash.png

# (str) iOS icons
ios.icons = 152,76,40,80,57,29,50,58,114,72,144,60,120,76,152,76,76,40,80

# (bool) Use iPhone 6 style fallback
ios.iphone6_fallback = False

# (str) iOS extra plist entries
ios.plist_strings =

# (str) XML files to include
android.add_xml = 

# (str) XML files to include
ios.add_xml = 

# (list) Android Gradle plugins to add
android.gradle_add_plugins = 

# (str) buildozer action (release, debug, etc.)
# android_arch = armeabi-v7a

# (str) Android entry point
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
# android.app_theme = "@style/MyAppTheme"

# (str) Android app theme (also add it to the drawable folder)
# android.app_theme = "apptheme"
# android.add_src = java

# (bool) Enable Logcat logging from python
# android.logcat = False

# (int) Android API to use for minification
# android.minapi.minify = 21

# (str) Unchanged assets
# unchanged_assets = None

# (bool) NACL build
# nacl = False

# (str) python-for-android fork to use, defaults to Kivy's
# p4a.fork = /path/to/your/fork

