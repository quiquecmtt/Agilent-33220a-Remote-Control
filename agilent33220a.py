# By Enrique Quik-e Cametti
import time
import numpy as np
import visa

class instrument:
    def __init__(self, visa_instrument_handle):
        self.instrument_handle = visa_instrument_handle
        self.memory=65536
        self.namelen=12
        self.vmax=10.0 # High Z
        self.freqmax=1000000.0 #[Hz] Arbs
        self.connected=0
        self.lentext=40
        self.noerror="ERROR"
        self.nospace="+0\n"

    def write(self, command_string): # Implements visa write command
        self.instrument_handle.write(command_string)

    def query(self, command_string): # Implements visa query command
        return self.instrument_handle.query(command_string)

    def read(self): # Implements visa read command
        return self.instrument_handle.read()

    def load_signal(self,V=0,name="VOLATILE"): # Instrument, Samples (floats) [-1;1], Name of the function
        if self.connected:
            if len(V)>self.memory:
                print("ERROR: Too many samples. (MAXIMUM MEMORY SAMPLES: {}.)".format(self.memory))
                print("Use V=V[:(-len(V)+self.memory)] to shorten the amount of samples.")
                self.write("DISPlay:TEXT \"ERROR: Too many samples.\"")
                time.sleep(2.5)
                self.write("DISPlay:TEXT:CLEAR")
                return
            name=name.upper()
            if V is not 0: # Looking if the input was an only one sample of values 0
                if np.amax(np.absolute(V)) is not 1:
                    print("Normalizing Arbitrary Function...")
                    self.write("DISPlay:TEXT \"Normalizing Arbitrary Function...\"")
                    V=V/np.amax(np.absolute(V))
                    time.sleep(2)
                    self.write("DISPlay:TEXT:CLEAR")
                if name=="VOLATILE":
                    print("Loading AF in volatile memory...")
                    self.write("DISPlay:TEXT \"Loading AF in volatile memory...\"")
                    charray=[]
                    for samples in V:
                        charray.append((samples)) # Adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
                    V=str(charray) # Paso de vars a chars
                    V=V.replace(V[0],"") # Take out '['
                    V=V.replace(V[-1],"") # Take out ']'
                    error="error"
                    while error != self.noerror:
                        error=self.query("SYSTem:ERRor?")
                    self.write("DATA VOLATILE,{}".format(V))
                    # Ver como se comprueba si se cargo
                    if self.query("SYSTem:ERRor?") == self.noerror:
                        print("***LOAD SUCCESSFUL***")
                        self.write("DISPlay:TEXT \"***LOAD SUCCESSFUL***\"")
                        time.sleep(2.5)
                        self.write("DISPlay:TEXT:CLEAR")
                    else:
                        print("***LOAD FAILED***")
                        self.write("DISPlay:TEXT \"***LOAD FAILED***\"")
                        time.sleep(2.5)
                        self.write("DISPlay:TEXT:CLEAR")
                        return
                else:
                    if self.query("DATA:NVOLatile:FREE?") != self.nospace:
                        if name[0].isalpha() != 1:
                            print("ERROR: Name must start with a letter.")
                            self.write("DISPlay:TEXT \"ERROR: Name must start with a letter.\"")
                            time.sleep(2.5)
                            self.write("DISPlay:TEXT:CLEAR")
                            return
                        if len(name)>12:
                            print("ERROR: Maximum name length is {} characters.".format(self.namelen))
                            self.write("DISPlay:TEXT \"ERROR: Maximum name length is {} characters.\"".format(namelen))
                            time.sleep(2.5)
                            print("Shortening name...")
                            self.write("DISPlay:TEXT \"Shortening name...\"")
                            name=name[:-leng(name)+self.namelen]
                            time.sleep(0.2)
                            print("Name shortened.")
                            self.write("DISPlay:TEXT \"Name shortened.\"")
                        for i in range(0,len(name)):
                            if name[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
                                name.replace(name[i],"")
                        catalog=self.query("DATA:CATalog?")
                        if name in catalog:
                            print("Another AF with the same name already exists in the catalog.")
                            print("Would you like to overwrite it? [Y/N]")
                            answer=input()
                            while answer.upper() not in "YN":
                                print("Please insert one of the options. [Y/N].")
                                answer=input()
                            if answer.upper()=="N":
                                print("***LOAD ABORTED***")
                                return;
                        print("Loading AF in volatile memory...")
                        self.write("DISPlay:TEXT \"Loading AF in volatile memory...\"")
                        charray=[]
                        for samples in V:
                            charray.append((samples)) # Adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
                        V=str(charray) # From floats to chars
                        V=V.replace(V[0],"") # Take out '['
                        V=V.replace(V[-1],"") # Take out ']'
                        error="error"
                        while error != self.noerror:
                            error=self.query("SYSTem:ERRor?")
                        self.write("DATA VOLATILE,{}".format(V))
                        if self.query("SYSTem:ERRor?") == self.noerror:
                            print("***LOAD SUCCESSFUL***")
                            self.write("DISPlay:TEXT \"***LOAD SUCCESSFUL***\"")
                            time.sleep(2.5)
                            self.write("DISPlay:TEXT:CLEAR")
                        else:
                            print("***LOAD FAILED***")
                            self.write("DISPlay:TEXT \"***LOAD FAILED***\"")
                            time.sleep(2.5)
                            self.write("DISPlay:TEXT:CLEAR")
                            return
                        name=name.replace(" ","_")
                        print("Copying AF to non-volatile memory...")
                        self.write("DISPlay:TEXT \"Copying AF to non-volatile memory...\"")
                        while error != self.noerror:
                            error=self.query("SYSTem:ERRor?")
                        self.write("DATA:COPY {}, VOLATILE".format(name))
                        time.sleep(0.5)

                        if self.query("SYSTem:ERRor?") == self.noerror:
                            print("***AF COPIED***")
                            self.write("DISPlay:TEXT \"***AF COPIED***\"")
                            time.sleep(2.5)
                            print("AF saved as \"{}\"".format(name))
                            time.sleep(2.5)
                            self.write("DISPlay:TEXT:CLEAR")
                        else:
                            print("***COPY FAILED***")
                            self.write("DISPlay:TEXT \"***COPY FAILED***\"")
                            time.sleep(2.5)
                            self.write("DISPlay:TEXT:CLEAR")
                            return
                    else:
                        print("Non-volatile memory is full. Need to erase one arbitrary function.")
                        self.write("DISPlay:TEXT \"Non-volatile memory is full. Need to erase one arbitrary function.\"")
                        time.sleep(2.5)
                        self.write("DISPlay:TEXT:CLEAR")
            return
        else:
            print("Please connect the device using connect_device().")

    def output_af(self,name="nonamewritten",amp=1,freq=1,Voffset=0): # Name of the Arbitrary Function, Amplitude in Vpp, Frequency in Hz, Voffset in V
        if self.connected:
            name=name.upper()
            amp=np.absolute(amp)
            freq=np.absolute(freq)
            if name=="nonamewritten":
                print("Must enter the name of the arbitrary function.")
                print("Catalog:",self.query("DATA:CATalog?"))
                return
            catalog=self.query("DATA:CATalog?")
            if name in catalog:
                self.write("OUTPUT:LOAD INFinity") # High Z
                if amp/2>self.vmax:
                    print("ERROR: VPP surpasses {}V.".format(self.vmax))
                    amp=self.vmax*2
                    print("New VPP: {}V".format(amp))
                if np.absolute(Voffset)>self.vmax-amp/2:
                    print("ERROR: |VPP/2|+|Voffset| surpasses {}V.".format(self.vmax))
                    Voffset=(self.vmax-amp/2)*Voffset/np.absolute(Voffset)
                    print("New Voffset: {}V".format(Voffset))
                if freq>self.freqmax:
                    print("ERROR: Frequency too high.")
                    freq=self.freqmax
                    print("New FREQ: {}kHz".format(freq/1000))
                self.write("FUNCtion:USER {}".format(name)) # Selects which arbitrary function I want
                self.write("FUNCtion USER") # Selects to use the USER function prevously chosen
                self.write("FREQuency {}".format(freq)) # Sets frequency
                self.write("VOLTage {}".format(amp)) # Sets Amplitude (in Vpp)
                self.write("VOLTage:OFFSet {}".format(Voffset)) # Sets offset
                self.write("DATA:TEXT \"{} selected.\"".format(name))
            else:
                print("Name isn't in catalog.")
                print("Catalog:",self.query("DATA:CATalog?"))
                return
        else:
            print("Please connect the device using connect_device().")

    def af_attributes(self,name="nonamewritten"):
        if self.connected:
            if name=="nonamewritten":
                print("Must enter the name of the arbitrary function.")
                print("Catalog:",self.query("DATA:CATalog?"))
                return
            name=name.upper()
            catalog=self.query("DATA:CATalog?")
            if name in catalog:
                print(f"{name} points:",self.query("DATA:ATTRibute:POINts? {}".format(name)))
                print(f"{name} average:",self.query("DATA:ATTRibute:AVERage? {}".format(name)))
                print(f"{name} cfactor:",self.query("DATA:ATTRibute:CFACtor? {}".format(name)))
                print(f"{name} ptpeak:",self.query("DATA:ATTRibute:PTPeak? {}".format(name)))
        else:
            print("Please connect the device using connect_device().")

    def erase_af(self,name):
        if self.connected:
            catalog=self.query("DATA:CATalog?")
            name=name.upper()
            if name in catalog:
                print("Are you sure yoou want to erase {}? [Y/N]".format(name))
                answer=input()
                while answer.upper() != "Y" and answer.upper() != "N":
                    print("Please insert one of the options. [Y/N].")
                    answer=input()
                if answer.upper()=="N":
                    print("***ERASE ABORTED***")
                    return
                self.write("OUTPUT OFF")
                self.write("FUNCtion SIN") # Selects to use the USER function prevously chosen
                error="error"
                while error != self.noerror:
                    error=self.query("SYSTem:ERRor?")
                self.write("DATA:DELete {}".format(name))
                if self.query("SYSTem:ERRor?") == self.noerror:
                    print("***ERASE SUCCESSFUL***")
                    self.write("DISPlay:TEXT \"***ERASE SUCCESSFUL***\"")
                    time.sleep(2.5)
                    self.write("DISPlay:TEXT:CLEAR")
                else:
                    print("***ERASE FAILED***")
                    self.write("DISPlay:TEXT \"***ERASE FAILED***\"")
                    time.sleep(2.5)
                    self.write("DISPlay:TEXT:CLEAR")
                    return
        else:
            print("Please connect the device using connect_device().")

    def display_text(self,text, tim=0):
        if self.connected:
            if len(text)>self.lentext:
                print("ERROR: Maximum char quantity ({}) exceeded.".format(self.lentext))
                self.write("DISPlay:TEXT \"ERROR: Maximum char quantity ({}) exceeded.\"")
            else:
                self.write("DISPlay:TEXT \"{}\"".format(text))
            if tim > 0:
                time.sleep(tim)
                self.write("DISPlay:TEXT:CLEAR")
        else:
            print("Please connect the device using connect_device().")

    def output_on(self):
        if self.connected:
            self.write("OUTPUT ON")
        else:
            print("Please connect the device using connect_device().")

    def output_off(self):
        if self.connected:
            self.write("OUTPUT OFF")
        else:
            print("Please connect the device using connect_device().")

    def catalog(self):
        if self.connected:
            catalog=self.query("DATA:CATalog?")
            print("Catalog:",catalog)
        else:
            print("Please connect the device using connect_device().")



def connect_device(): # No se si funciona
    rm = visa.ResourceManager('@ni')   # @ni loads national instruments, @py loads pyvisa
    print(rm.list_resources())
    inst_handle = rm.open_resource(rm.list_resources()[0])
    inst_handle.timeout=40000
    connect=instrument(inst_handle)
    connect.connected=1
    connect.write("*CLS")
    connect.noerror=connect.query("SYSTem:ERRor?")
    print("***INSTRUMENT CONNECTED***")
    connect.write("DISPlay:TEXT \"***INSTRUMENT CONNECTED***\"")
    time.sleep(1.5)
    return connect
