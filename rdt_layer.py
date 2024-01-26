from segment import Segment
import copy

# #################################################################################################################### #
# RDTLayer                                                                                                             #
#                                                                                                                      #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
#                                                                                                                      #
#                                                                                                                      #
# Notes:                                                                                                               #
# This file is meant to be changed.                                                                                    #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    DATA_LENGTH = 4 # in characters                     # The length of the string data that will be sent per packet...
    FLOW_CONTROL_WIN_SIZE = 15 # in characters          # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0                                # Use this for segment 'timeouts'
    # TODO: Add items as needed
    dataReceived = ''                                   # Created for part 1 of the assignment, somewhere to hold our received data

    currentSequenceNumber = 1                           # Created for part 2 as a way to hold the sequence number as a global (no changing on each call), will change to string in function
    segmentBuffer = list()                              # Created for part 2, buffer to hold each piece of the string for easy access

    currentWindowSize = 0                               # Increased in part 2, decreased in part 3, Created to find out how much space is in the window
    memoryBuffer = dict()                               # Used in part 2, Created this so that the system can create a dictionary of the data stream and it's ack for lost packages
    ackBuffer = list()                                  # Used in part 3, Created this so that client/server could add what has been acknowledged and what hasn't (if in list, it has been ACK'd)

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def __init__(self):
        self.sendChannel = None
        self.receiveChannel = None
        self.dataToSend = ''
        self.currentIteration = 0
        # Add items as needed

    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data

    # Created for part 1 of the assignment, need to set our new variable to some value
    def setDataReceived(self, string):
        self.dataReceived = string

    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    # TODO: This spot (it's a getter function, needs a setter(setDataReceived) and some variable(dataReceived))
    def getDataReceived(self):
        # ############################################################################################################ #
        # Identify the data that has been received...
        # print('getDataReceived(): Complete this...')
        # ############################################################################################################ #
        return self.dataReceived

    # ################################################################################################################ #
    # processData()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    # TODO: This spot
    def processSend(self):
        # Code that was commented out and tabbed
            # segmentSend = Segment()     # TODO: May have to move

        # ############################################################################################################ #
        print('processSend(): Complete this...')

        print("  CURRENT WINDOW SIZE:", self.currentWindowSize)

        '''
        PSEUDOCODE
        if "there is space to create segments" (windowSize - currentSize):
            segmentX = Segment()
            while i++ <= 4 AND "space in window":
                string += "next character in dataToSend"
            segmentX.setData(seqnum, string)
            self.sendChannel.send(segmentX)
            if "window still has space":
                "do it again"
        
        May need to use copy() function to copy the segmentX and send that copy along
        so copiedSegment = segmentX.copy()
        copiedSegment.send()
        self.sendChannel.send(copiedSegment)
        OR
        something like what was suggested by TA
        self.sendChannel.send(copy.copy(segmentSend/segmentX))
        '''

        '''
        # You should pipeline segments to fit the flow-control window
        # The flow-control window is the constant RDTLayer.FLOW_CONTROL_WIN_SIZE
        # The maximum data that you can send in a segment is RDTLayer.DATA_LENGTH
        # These constants are given in # characters

        # Somewhere in here you will be creating data segments to send.
        # The data is just part of the entire string that you are trying to send.
        # The seqnum is the sequence number for the segment (in character number, not bytes)
        '''

        # NEW STUFF GOES HERE (2nd ATTEMPT) :: CODE HERE

        '''
        # Add the data to send into a buffer, based on pos+1 will be the sequence number
            # Learned that you can access elements of a string like a list (ie string[0] = 'h'),
            # removing this and changing data+=self.dataBuffer to data+=self.dataToSend made no difference to the output
            # meaning that it should be fine to remove this and the global
        # if not self.dataBuffer:
        #     self.dataBuffer = list(self.dataToSend)
        '''

        # Is there is data to send AND there is still data to be sent # TODO: May need to remove the if statement
        if self.dataToSend and self.currentSequenceNumber < len(self.dataToSend):
            # Check if there is space to create a segment
            # currentWindowSize start at 0
            # currentSequenceNumber starts at 1
            while self.currentWindowSize < self.FLOW_CONTROL_WIN_SIZE:
                # Create the segment, will overwrite last segment object
                segmentSend = Segment()

                # Figure out size of data stream so we know how many characters are being sent
                numberOfCharacters = self.FLOW_CONTROL_WIN_SIZE - self.currentWindowSize
                if numberOfCharacters > 4:
                    numberOfCharacters = 4
                # Else it is just the size

                # Increase size of the window for the while loop and other checks
                self.currentWindowSize += numberOfCharacters

                # Create the data variable that we will be sending
                data = ""
                seqnum = str(self.currentSequenceNumber)    # Do this before incrementing the sequence Number
                for i in range(numberOfCharacters):
                    data += self.dataToSend[self.currentSequenceNumber - 1]
                    self.currentSequenceNumber += 1

                # Add to the memory buffer what was sent # TODO: May need to delete following chunk later
                # It saves to the buffer dictionary ["data sequence" : sequence number start]
                self.memoryBuffer[data] = self.currentSequenceNumber - numberOfCharacters
                # To access element of dictionary later do this: first_value = list(self.memoryBuffer.values())[0]

                # Set the data for the segment, printout what we are sending them, then send it
                segmentSend.setData(seqnum, data)
                self.segmentBuffer.append(segmentSend)  # TODO: May need to delete later
                print("Sending segment: ", segmentSend.to_string())
                self.sendChannel.send(copy.copy(segmentSend))   # Copy because python is pass-by-reference-object


        '''
        # PREVIOUS STUFF (1st ATTEMPT)
        # Create a buffer of values for the string segments if needed (if empty, do loop)
        if not self.dataBuffer:
            self.dataBuffer = [self.dataToSend[i:i+4] for i in range(0, len(self.dataToSend), 4)]
            self.dataAcks = [0] * len(self.dataBuffer)
            print("I created it")
        else:
            print("I skipped it")
        for i in range(len(self.dataBuffer)):
             print("i is", i, "and the element of that is: ", self.dataBuffer[i])
        # if self.dataBuffer:
        #     print("Current buffer piece is: ", self.dataBuffer[0])
        '''

        '''
        # Code that was commented out and tabbed
            # seqnum = "0"
            # data = "x"

        # ############################################################################################################ #
        # Display sending segment
            # segmentSend.setData(seqnum,data) # TODO: May have to move
            # print("Sending segment: ", segmentSend.to_string())

        # Use the unreliable sendChannel to send the segment
            # self.sendChannel.send(segmentSend) # TODO: May have to move
        '''

    # ################################################################################################################ #
    # processReceive()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    # TODO: This spot
    def processReceiveAndSendRespond(self):
        # May need to move this
            # segmentAck = Segment()    # Segment acknowledging packet(s) received

        # This call returns a list of incoming segments (see Segment class)...
        listIncomingSegments = self.receiveChannel.receive()
        # Priming the variable for later
        expectedSequence = 1

        # ############################################################################################################ #
        # What segments have been received?
        # How will you get them back in order?
        # This is where a majority of your logic will be implemented
        print('processReceive(): Complete this...')

        '''
        acknum = "0"
        print(listIncomingSegments)
        if listIncomingSegments:
            # Why does adding the next line make the list None????
            # listIncomingSegments = listIncomingSegments.sort(key=lambda x: int(x.seqnum))  # This is to sort an unordered list
            for i in listIncomingSegments:
                print("The word:", i.to_string())
                self.dataReceived += i.payload  # NEED THIS
            print("The segment I am trying to ACK:", listIncomingSegments[-1].payload)
            acknum = listIncomingSegments[-1].seqnum + len(listIncomingSegments[-1].payload)
            print("The toString thing:", listIncomingSegments[0].to_string())
        '''

        '''
        # STUFF GOES HERE (1st ATTEMPT) :: CODE HERE
        
        # Are there any received items, if so loop through them
        if listIncomingSegments:
            # Loop through each segment element in the list
            for i in listIncomingSegments:
                # Create a new segment that we will be packing up
                segmentAck = Segment()

                # If the sequence I received is equal to what I was expecting
                if i.seqnum == expectedSequence:
                    acknum = expectedSequence               # Set the ack number to the sequence
                    expectedSequence += len(i.payload)      # Change the expected to the next sequence

                    # If this is a segment I was expecting earlier, send the buffer and empty it
                    if self.ackBuffer:
                        # Sequence number is finally what was expected, however there is stuff in the buffer that needs to be cleaned out
                        # Send the packet that we received, which is in the correct order
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(segmentAck)

                        # Loop through and send all the other segments that we were buffering
                        for j in self.ackBuffer:
                            segmentAck = j.pop(0)
                            # segmentAck.setAck(j.seqnum)   # We don't need to send the ACK for each packet, just the one we wanted
                            self.sendChannel.send(copy.copy(segmentAck))
                    else:
                        # Sequence number is what was expected AND there is nothing in the buffer to worry about
                        self.dataReceived += i.payload  # NEED THIS
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(copy.copy(segmentAck))
                else:
                    # Otherwise, we still want to send an ACK but because it is not what we expected we pack up the segment to be sent again later
                    acknum = i.seqnum
                    self.ackBuffer.append(i)
                    segmentAck.setAck(str(acknum))
                    print("Sending ack: ", segmentAck.to_string())
                    self.sendChannel.send(copy.copy(segmentAck))
        '''

        '''
        # STUFF GOES HERE (2nd ATTEMPT) :: CODE HERE
        if listIncomingSegments:
            print("Current list of objects")
            for i in listIncomingSegments:
                print(" ", i.to_string())

        # Are there any received items, if so loop through them
        if listIncomingSegments:
            # Loop through each segment element in the list
            for i in listIncomingSegments:
                segmentAck = Segment()
                # print("The segment:", i.to_string())

                # If the sequence I received is equal to what I was expecting
                if int(i.seqnum) == expectedSequence or int(i.acknum) == expectedSequence:
                    acknum = expectedSequence  # Set the ack number to the sequence
                    expectedSequence += len(i.payload)  # Change the expected to the next sequence

                    # print(" I got the sequence I expected!")
                    # print(" The new expectedSequence is:", expectedSequence)

                    # If this is a segment I was expecting earlier, send the buffer and empty it
                    if self.ackBuffer:
                        # Sequence number is finally what was expected, however there is stuff in the buffer that needs to be cleaned out
                        # Send the packet that we received, which is in the correct order
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(segmentAck)

                        # Loop through and send all the other segments that we were buffering
                        for j in self.ackBuffer:
                            segmentAck = self.ackBuffer.pop(0)
                            # segmentAck.setAck(j.seqnum)   # We don't need to send the ACK for each packet, just the one we wanted
                            self.sendChannel.send(copy.copy(segmentAck))
                    else:
                        # Sequence number is what was expected AND there is nothing in the buffer to worry about
                        self.dataReceived += i.payload  # NEED THIS
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(copy.copy(segmentAck))
                else:
                    # Otherwise, we still want to send an ACK but because it is not what we expected we pack up the segment to be sent again later
                    acknum = i.seqnum
                    self.ackBuffer.append(i)
                    segmentAck.setAck(str(acknum))
                    print("Sending ack: ", segmentAck.to_string())
                    self.sendChannel.send(copy.copy(segmentAck))
        '''

        # STUFF GOES HERE (3rd ATTEMPT) :: CODE HERE

        # Are there any received items, if so loop through them
        if listIncomingSegments:
            # Is what I got a Segment, else its an ACK
            if listIncomingSegments[0].acknum == -1:
                # Loop through each segment element in the list
                for i in listIncomingSegments:
                    segmentAck = Segment()
                    # print("The segment:", i.to_string())

                    # If the sequence I received is equal to what I was expecting
                    if int(i.seqnum) == expectedSequence or int(i.acknum) == expectedSequence:
                        acknum = expectedSequence  # Set the ack number to the sequence
                        expectedSequence += len(i.payload)  # Change the expected to the next sequence

                        # print(" I got the sequence I expected!")
                        # print(" The new expectedSequence is:", expectedSequence)

                        # If this is a segment I was expecting earlier, send the buffer and empty it
                        if self.ackBuffer:
                            # Sequence number is finally what was expected, however there is stuff in the buffer that needs to be cleaned out
                            # Send the packet that we received, which is in the correct order
                            segmentAck.setAck(str(acknum))
                            print("Sending ack: ", segmentAck.to_string())
                            self.sendChannel.send(segmentAck)

                            # Loop through and send all the other segments that we were buffering
                            for j in self.ackBuffer:
                                segmentAck = self.ackBuffer.pop(0)
                                # segmentAck.setAck(j.seqnum)   # We don't need to send the ACK for each packet, just the one we wanted
                                self.sendChannel.send(copy.copy(segmentAck))
                        else:
                            # Sequence number is what was expected AND there is nothing in the buffer to worry about
                            self.dataReceived += i.payload  # NEED THIS
                            segmentAck.setAck(str(acknum))
                            print("Sending ack: ", segmentAck.to_string())
                            self.sendChannel.send(copy.copy(segmentAck))
                    else:
                        # Otherwise, we still want to send an ACK but because it is not what we expected we pack up the segment to be sent again later
                        acknum = i.seqnum
                        self.ackBuffer.append(i)
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(copy.copy(segmentAck))
            else:
                # Else what I got was an ACK
                # Loop through each segment element in the list
                for i in listIncomingSegments:
                    # If this is an ACK I have not seen before, send a response ELSE log it
                    if i not in self.ackBuffer:
                        segmentAck = Segment()
                        acknum = i.acknum
                        segmentAck.setAck(str(acknum))
                        print("Sending ack: ", segmentAck.to_string())
                        self.sendChannel.send(copy.copy(segmentAck))

                        self.currentWindowSize -= len(i.payload)
                        self.ackBuffer.push(i)
                    else:
                        self.ackBuffer.pop(i)


        # ############################################################################################################ #
        # How do you respond to what you have received?
        # How can you tell data segments apart from ack segments?
        print('processReceive(): Complete this...')

        # Somewhere in here you will be setting the contents of the ack segments to send.
        # The goal is to employ cumulative ack, just like TCP does...
            # acknum = "0"

        # ############################################################################################################ #
        # Display response segment
            # segmentAck.setAck(acknum)
            # print("Sending ack: ", segmentAck.to_string())

        # Use the unreliable sendChannel to send the ack packet
            # self.sendChannel.send(segmentAck)
