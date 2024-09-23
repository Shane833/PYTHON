# The PyQt GUI's are Event Driven i.e. they respond to events
# created by the user with mouse and keyboard or by system such as 
# when connecting with bluetooth, so no matter how they are crated
# your application must handle them and this process is called Event handling

# Event handling in PyQt is done with the help of signal and slots
# Signals are the events that occurs when a widgets state changes 
# such as when a button is clicked or checkbox is toggled
# Slots are the users-defined or built-in PyQt functions that act as 
# a response to these signals

# Most of the PyQt elements have pre-defined signal and slots, so you can
# simply implement the required function to achieve the desired behaviour 
# from your application