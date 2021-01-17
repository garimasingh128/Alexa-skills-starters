import logging
import ask_sdk_core.utils as ask_utils
import random
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
actions=['spock','paper','scissor','lizard','rock']

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Here is Sheldon game, Lets start it, 3, 2, 1... What do you choose?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class GameIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GameIntent")(handler_input)

    def handle(self, handler_input):
        speak_output=""
        speak_output2=" What is your next move ?"
        slots = handler_input.request_envelope.request.intent.slots
        user_action=slots["action"].value
        num=random.randint(0,len(actions)-1)
        join=user_action+actions[num]
        join = join.lower()
        if join=='rockrock':
            speak_output="You played rock, and I played rock, it is a tie! "
        elif join=='rockpaper':
            speak_output="You played rock, and I played paper, I win! "
        elif join=='rockscissor':
            speak_output="You played rock, and I played scissor, Congratulations, you win!"
        elif join=='rocklizard':
            speak_output="You played rock, and I played lizard,rock crushes lizard. Congratulations, you win!"
        elif join=='rockspock':
            speak_output="You played rock, and I played spock,spock vaporizes rock.I win!"
        elif join=='paperrock':
            speak_output="You played paper, and I played rock, Congratulations, you win!"
        elif join=='paperpaper':
            speak_output="You played paper, and I played paper, it is a tie! "
        elif join=='paperscissor':
            speak_output="You played paper, and I played scissor, I win! "
        elif join=='paperlizard':
            speak_output="You played paper, and I played lizard,lizard eats paper. I win! "
        elif join=='paperspock':
            speak_output="You played paper, and I played spock,paper disproves spock. Congratulations you win! "
        elif join=='scissorrock':
            speak_output="You played scissor, and I played rock, I win! "
        elif join=='scissorpaper':
            speak_output="You played scissor, and I played paper, Congratulations, you win!"
        elif join=='scissorscissor':
            speak_output="You played scissor, and I played scissor, it is a tie! "
        elif join=='scissorlizard':
            speak_output="You played scissor, and I played lizard,scissors decapitates lizard.Congratulations you win! "
        elif join=='scissorspock':
            speak_output="You played scissor, and I played spock,spock smashes scissors.I win! "
        elif join=='lizardrock':
            speak_output="You played lizard, and I played rock,rock crushes lizard.I win! "
        elif join=='lizardpaper':
            speak_output="You played lizard, and I played paper, lizard eats paper.Congratulations you win! "
        elif join=='lizardscissor':
            speak_output="You played lizard, and I played scissor,scissors decapitates lizard.I win! "
        elif join=='lizardlizard':
            speak_output="You played lizard, and I played lizard,It's a tie! "
        elif join=='lizardspock':
            speak_output="You played lizard, and I played spock,lizard poisons spock.Congratulations you win! "
        elif join=='spockrock':
            speak_output="You played spock, and I played rock,spock vaporizes rock.Congratulations you win! "
        elif join=='spockpaper':
            speak_output="You played spock, and I played paper, paper disproves spock.I win! "
        elif join=='spockscissor':
            speak_output="You played spock, and I played scissor,spock smashes scissors.Congratulations you win! "
        elif join=='spocklizard':
            speak_output="You played spock, and I played lizard, lizard poisons spock.I win! "
        elif join=='spockspock':
            speak_output="You played spock, and I played spock.It's a tie! "
            
        else:
            speak_output2=""
            speak_output="Please choose the correct action."
            
            
            
        # type: (HandlerInput) -> Response
        
        

        return (
            handler_input.response_builder
                .speak(speak_output+speak_output2)
                .ask(speak_output2)
                .response
                
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Please choose any action among , Rock, Paper, Scissor ,lizard and spock."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "GoodBye!! See you soon..."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GameIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()