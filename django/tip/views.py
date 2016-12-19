from django.http import HttpResponse

from selenium import webdriver

def selenium_hatena_profile(request):
    browser = webdriver.PhantomJS()
    browser.implicitly_wait(3)
    browser.get(request.GET['url'])
    browser.get(browser.find_element_by_css_selector('a.hatena-id-link').get_attribute('href'))
    browser.get(browser.find_elements_by_css_selector('div.entry-content a')[0].get_attribute('href'))
    browser.save_screenshot('website.png')
    return HttpResponse([print('*', x) for x in
                         [p.text for p in browser.find_elements_by_css_selector('dl.profile dd.profile-dd p') if p] if
                         x])
