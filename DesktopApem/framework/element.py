class BaseElement(object):
    """From here comes everything"""

    def __init__(self, element):
        self.driver = element._parent  # fail if it's not a WebElement
        self.element = element

    @property
    def tag_name(self):
        return self.element.get_property('tagName')

    def find_element(self, locator):
        return self.element.find_element(locator)

    def get_property(self, property):
        return self.element.get_property(property)

    def set_attribute(self, attribute_name, attribute_value):
        driver = self.element._parent
        driver.execute_script("arguments[0].setAttribute('" + attribute_name + "', '" + attribute_value + "')", self.element)

    def get_attributes(self):
        '''return a dict that contains all attributes names as key and values as key value'''
        attributes_dict = self.get_property('attributes')
        return attributes_dict

    def click(self):
        self.scroll_to()
        try:
            self.element.click()
        except:  # if it's not clickable i.e. covered by other visible/invisible element
            self.element._parent.execute_script("arguments[0].click();", self.element)
        # self.element.click()

    def scroll_to(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)

    def exists(self):
        return self.element.is_displayed()

    def is_enabled(self):
        return self.element.is_enabled()