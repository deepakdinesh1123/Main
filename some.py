
from django.db import models
# importing validationerror
from django.core.exceptions import ValidationError


print("""
jobs:
  test:
    name: Run Unit Tests
    runs-on: ubuntu-18.04

    steps:
      - uses: actions/checkout@v1
      - name: set up JDK 1.8
        uses: actions/setup-java@v1
        with:
          java-version: 1.8
      - name: Unit tests
        run: bash ./gradlew test --stacktrace
      - name: Unit tests results
        uses: actions/upload-artifact@v1
        with:
          name: unit-tests-results
          path: app/build/reports/tests/testDebugUnitTest/index.html

  lint:
    name: Lint Check
    runs-on: ubuntu-18.04

    steps:
      - uses: actions/checkout@v1
      - name: set up JDK 1.8
        uses: actions/setup-java@v1
        with:
          java-version: 1.8
      - name: Lint debug flavor
        run: bash ./gradlew lintDebug --stacktrace
""")
print("self hosted runner added(ubuntu vm) and windows removed")
 
# creating a validator function
def validate_geeks_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")
 
 
# Create your models here.
class GeeksModel(models.Model):
    geeks_mail = models.CharField(max_length = 200)