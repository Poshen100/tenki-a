name: Flutter CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.24.0'
      - name: Install dependencies
        run: flutter pub get
      - name: Run tests
        run: flutter test
      - name: Build APK (optional)
        run: flutter build apk --release
