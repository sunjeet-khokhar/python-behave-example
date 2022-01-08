Feature: Google\'s Search Functionality
    Scenario: can find search results
        Given a Browser session is active
        When visit url "http://www.google.com/"
        '''When field with name "q" is given "TestingBot"
        Then title becomes "TestingBot - Google Search" '''
