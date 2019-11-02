from mycroft import MycroftSkill, intent_file_handler


class HomeassistantMqtt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mqtt.homeassistant.intent')
    def handle_mqtt_homeassistant(self, message):
        self.speak_dialog('mqtt.homeassistant')


def create_skill():
    return HomeassistantMqtt()

