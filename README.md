# Python-Exercise

## Selenium

## Installation

Selenium may be installed via npm with

    npm install selenium-webdriver

Selenium with python

    pip3 install selenium 

### Safari Import

    sudo safaridriver --enable
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    
### Using the Builder API

The `Builder` class is your one-stop shop for configuring new WebDriver
instances. Rather than clutter your code with branches for the various browsers,
the builder lets you set all options in one flow. When you call
`Builder#build()`, all options irrelevant to the selected browser are dropped:

    javascript
    const webdriver = require('selenium-webdriver');
    const chrome = require('selenium-webdriver/chrome');
    const firefox = require('selenium-webdriver/firefox');
    let driver = new webdriver.Builder()
        .forBrowser(webdriver.Browser.FIREFOX)
        .setChromeOptions(/* ... */)
        .setFirefoxOptions(/* ... */)
        .build();


### Selenium Download


| Browser           | Component                          |
| ----------------- | ---------------------------------- |
| Chrome            | [ChromeDriver][chrome]             |
| Firefox           | [GeckoDriver][firefox]             |
| Internet Explorer | [IEDriverServer][ie]               |
| Edge              | [MicrosoftWebDriver.msi][edge]     |
| Safari            | [SafariDocs][safari]               |


[firefox]: https://github.com/mozilla/geckodriver/releases/
[chrome]: http://chromedriver.storage.googleapis.com/index.html?path=102.0.5005.27/
[ie]: https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp
[edge]: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
[safari]: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari
