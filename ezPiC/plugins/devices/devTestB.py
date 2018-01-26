"""
...TestB...
"""
#import logging
import time
import Tool
import Device

###################################################################################################
# Globals:

DUID = 'TestB'
NAME = 'Readable Name B'
INFO = 'Fusce dolor leo, ornare vitae dolor nec, varius aliquam tellus. Phasellus mollis velit ut neque eleifend, sed gravida tellus placerat. Cras nisl sapien, gravida eget elit eu, facilisis fringilla erat. Nulla maximus ullamcorper tortor, quis vulputate est dapibus non. Aliquam dui sem, ultrices non nunc eu, molestie interdum diam. Ut rhoncus ipsum nisl. Nulla consequat convallis blandit. Morbi eu ipsum massa. Fusce id diam eget nisl tincidunt egestas maximus eget leo. Aenean nec erat vitae arcu posuere luctus id non turpis. Mauris ultricies nunc ante, id sollicitudin nulla tempus venenatis. Nulla facilisi. Vestibulum tincidunt nunc ac eros sollicitudin, in tincidunt ante porttitor. Duis a fermentum arcu. Nullam sollicitudin facilisis rhoncus. Nam gravida arcu in tortor dapibus, eu congue purus vehicula.'

BBB = 1

###################################################################################################

class PluginDevice(Device.PluginDeviceBase):
    """ TODO """

    def __init__(self, module):
        super().__init__(module)
        self.param = {'abc':12345, 'xyz':67890}
        self.timer_period = 5.5555

    def timer(self):
        print('B' + str(time.time()))

###################################################################################################
###################################################################################################
###################################################################################################
