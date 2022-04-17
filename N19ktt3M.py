import datetime

class Schedule:
    '''Represents a recording rule from .cvs file'''

    highres = ""
    days = ""
    startTime = ""
    endTme = ""

    def __init__(self, baseName, channel, days, startTime, endTime, highres):
        self.baseName = baseName
        self.channel = channel
        self.recordToday = False
        self.highres = False
        self.startTime = datetime.datetime.strptime(startTime, "%H%M%S").time()
        self.endTime = datetime.datetime.strptime(endTime, "%H%M%S").time()


        # Check for highres and turn into a boolean
        if highres.lower() in ("y", "ye", "yes"):
            self.highres = True
        else:
            self.recordToday = False

        # Check if show should be recorded today
        d = datetime.datetime.now()
        if days.lower().find('mo') != -1:
            if d.isoweekday() == 1:
                self.recordToday = True
        if days.lower().find("tu") != -1:
            if d.isoweekday() == 2:
                self.recordToday = True
        if days.lower().find("we") != -1:
            if d.isoweekday() == 3:
                self.recordToday = True
        if days.lower().find("th") != -1:
            if d.isoweekday() == 4:
                self.recordToday = True
        if days.lower().find("fr") != -1:
            if d.isoweekday() == 5:
                self.recordToday = True
        if days.lower().find("sa") != -1:
            if d.isoweekday() == 6:
                self.recordToday = True
        if days.lower().find("su") != -1:
            if d.isoweekday() == 7:
                self.recordToday = True


# Testing data, this will only run if the module is ran from the cli, not imported
if __name__ == '__main__':
    sch = Schedule("My Program", "7.1", "MoTuWeThFrSaSu", "165900", "173100", "n" )

    print ("Base name is: {}".format(sch.baseName()))
    print ("Channel is: {}".format(sch.channel()))
    print ("Record today?: {}".format(sch.recordToday()))
    print ("Start time is: {}".format(sch.startTime()))
    print ("End time is: {}".format(sch.endTime()))
    print ("Highres is: {}".format(sch.highres()))