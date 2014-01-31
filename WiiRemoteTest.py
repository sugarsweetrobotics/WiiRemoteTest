#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file WiiRemoteTest.py
 @brief Test Component
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import os
def cls():
    os.system(['clear','cls'][os.name == 'nt'])


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
wiiremotetest_spec = ["implementation_id", "WiiRemoteTest", 
		 "type_name",         "WiiRemoteTest", 
		 "description",       "Test Component", 
		 "version",           "1.0.0", 
		 "vendor",            "Sugar Sweet Robotics", 
		 "category",          "Tutorial", 
		 "activity_type",     "DataFlowComponent", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class WiiRemoteTest
# @brief Test Component
# 
# 
class WiiRemoteTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_buttons = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		"""
		self._buttonsIn = OpenRTM_aist.InPort("buttons", self._d_buttons)
		self._d_accel = RTC.TimedAngularAcceleration3D(RTC.Time(0,0),0)
		"""
		"""
		self._accelIn = OpenRTM_aist.InPort("accel", self._d_accel)
		self._d_orientation = RTC.TimedOrientation3D(RTC.Time(0,0),0)
		"""
		"""
		self._orientationIn = OpenRTM_aist.InPort("orientation", self._d_orientation)
		self._d_cursor = RTC.TimedPoint2D(RTC.Time(0,0),0)
		"""
		"""
		self._cursorIn = OpenRTM_aist.InPort("cursor", self._d_cursor)
		self._d_distance = RTC.TimedLong(RTC.Time(0,0),0)
		"""
		id
		"""
		self._distanceIn = OpenRTM_aist.InPort("distance", self._d_distance)
		self._d_ir = RTC.TimedPoint2D(RTC.Time(0,0),0)
		"""
		"""
		self._irIn = OpenRTM_aist.InPort("ir", self._d_ir)
		self._d_rumble = RTC.TimedBoolean(RTC.Time(0,0),0)
		"""
		"""
		self._rumbleOut = OpenRTM_aist.OutPort("rumble", self._d_rumble)
		self._d_leds = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		"""
		self._ledsOut = OpenRTM_aist.OutPort("leds", self._d_leds)

                """
		self.buttons = [False] * 12
		self.cursor  = [0, 0]
		self.ir      = [0, 0]
		self.distance = 0
		self.accel   = [0, 0, 0]
		self.orientation = [0, 0, 0]
		"""
		self.rumble = False
		self.leds   = [False] * 4


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("buttons",self._buttonsIn)
		self.addInPort("accel",self._accelIn)
		self.addInPort("orientation",self._orientationIn)
		self.addInPort("cursor",self._cursorIn)
		self.addInPort("distance",self._distanceIn)
		self.addInPort("ir",self._irIn)
		
		# Set OutPort buffers
		self.addOutPort("rumble",self._rumbleOut)
		self.addOutPort("leds",self._ledsOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	def onActivated(self, ec_id):
            self.buttons = [False] * 11
            self.accel = RTC.AngularAcceleration3D(0, 0, 0)
            self.orientation = RTC.Orientation3D(0, 0, 0)
            self.cursor = RTC.Point2D(0, 0)
            self.distance = 0
            self.ir = RTC.Point2D(0, 0)
            return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):

                if self._buttonsIn.isNew():
                    data = self._buttonsIn.read()
                    self.buttons = data.data

                if self._accelIn.isNew():
                    data = self._accelIn.read()
                    self.accel = data.data

                if self._orientationIn.isNew():
                    data = self._orientationIn.read()
                    self.orientation = data.data

                if self._irIn.isNew():
                    data = self._irIn.read()
                    self.ir = data.data

                if self._cursorIn.isNew():
                    data =  self._cursorIn.read()
                    self.cursor = data.data


                sys.stdout.write('[WiiRemoteTest] buttons:')
                for b in self.buttons:
                    sys.stdout.write('T' if b else 'F')
                sys.stdout.write('\n')
                
                sys.stdout.write('[WiiRemoteTest] accel: aax=%3.3f, aay=%3.3f, aaz=%3.3f\n' % (self.accel.aax, self.accel.aay, self.accel.aaz))
                sys.stdout.write('[WiiRemoteTest] orientation: r=%3.3f, p=%3.3f, y=%3.3f\n' % (self.orientation.r, self.orientation.p, self.orientation.y))
                sys.stdout.write('[WiiRemoteTest] cursor: x=%3.3f, y=%3.3f\n' % (self.cursor.x, self.cursor.y))
                sys.stdout.write('[WiiRemoteTest] distance: d=%3.3f\n' % self.distance)
                sys.stdout.write('[WiiRemoteTest] ir: x=%3.3f, y=%3.3f\n' % (self.ir.x, self.ir.y))

		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def WiiRemoteTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=wiiremotetest_spec)
    manager.registerFactory(profile,
                            WiiRemoteTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    WiiRemoteTestInit(manager)

    # Create a component
    comp = manager.createComponent("WiiRemoteTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
	main()

