
#неправильный вид кода
from abc import ABCMeta, abstractmethod
class CommunicationDevice():
  @abstractmethod
  def make_calls():
    pass

  @abstractmethod
  def send_sms():
    pass

  @abstractmethod
  def browse_internet():
    pass

class SmartPhone(CommunicationDevice):
  def make_calls():
    pass

  def send_sms():
    pass

  def browse_internet():
    pass

  class LandlinePhone(CommunicationDevice):
    def make_calls():
      pass

    def send_sms():
      pass

    def browse_internet():
      pass

#правильный вид кода
from abc import ABCMeta, abstractmethod
class CallingDevice():
    @abstractmethod
    def make_calls():
        pass


class MessagingDevice():
    @abstractmethod
    def send_sms():
        pass


class InternetbrowsingDevice():
    @abstractmethod
    def browse_internet():
        pass


class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
    def make_calls():
        pass

    def send_sms():
        pass

    def browse_internet():
        pass


class LandlinePhone(CallingDevice):
    def make_calls():
        pass