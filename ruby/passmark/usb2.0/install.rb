require 'fileutils'
require 'find'
require 'win32ole'

# check OS 32 or 64 bit  str
def Check_OS_Bit()
	if File.directory?("C:\\Program Files (x86)")
		puts("OS is 64 bit")
		os_bit = "x64"
		return os_bit
	else
		puts("OS is 32 bit")
		os_bit = "x86"
		return os_bit
	end
end

# check OS version    str
def Check_OS_Version()
	os_version = `ver`
	return os_version
end


# check if device exist   bool
def Check_Device()
	if File.directory?("c:\\Drvpack64")
		`C:\\Drvpack64\\Autobot\\utils\\sutconfig`
	else
		`C:\\Drvpack\\Autobot\\utils\\sutconfig`
	end
	flag = 0
	File.open("C:\\Users\\Administrator\\AppData\\Local\\Temp\\config.txt","r") do |c_file|
		while cline = c_file.gets  
			list = cline.split(" ")
			did = list[1]
			vid = list[2]
			File.open("C:\\Users\\Administrator\\AppData\\Local\\Temp\\device.txt","r") do |sut_file|
				while sline = sut_file.gets
					if  did != nil and sline.include?("VID_0403") and sline.include?(did)  # need to change according to the vendor
						flag = 1
						puts("Device found")
						puts sline
					end
				end
			end
		end
		if flag == 0
			puts "Cannot find the device"
			return false
		else
			return true
		end				
	end
end

# get driver name  str
def Get_Driver_Name()
	driver_name = 11
	Dir.foreach(Dir.getwd){ |fn| if /zip$/.match(fn) or /rar$/.match(fn) or /7z$/.match(fn)
							driver_name = fn
							end
							
	}
	return driver_name
end

# check if drive installed  bool
def Check_Driver_Installed(name)
	driver_installed = false
	Dir.foreach(File.dirname(Dir.getwd)){|fn| if fn == "driverInstallLog.txt"
												#puts fn
												file = File.open("..\\driverInstallLog.txt","r")
												file.each{|line| if line.include? name
																	driver_installed = true
																 end
												}
											   end
										}
										
	return driver_installed
end

# write log   
def Write_Log(log)
	Dir.chdir("C:\\Users\\Administrator\\AppData\\Local\\Temp")
	file = File.new("driverInstallLog.txt","a+") 
	file.syswrite(log)
	file.syswrite("\n")
	file.close											
end

#unzip the package
def unzip(name)
	rc = -1
	`unzip -o -q #{name} > nul` 
	if $?.exitstatus == 0
		rc = 0
	else
		rc = 900  # unzip fail
	end
	return rc
end


# main
if Check_Device() == true
		rc = -1
		drivername = Get_Driver_Name()
		puts(drivername)
		driver_installed = Check_Driver_Installed(drivername)
		if driver_installed == false
			rc = unzip(drivername)
#			puts rc
#			puts (Dir.getwd())
			system('start CloseSecurityWindow.exe')
			if rc == 0
#				Dir.chdir(".\\usb3loopdriver_1.2.3\\win7")      # need to change according to the driver
#				osbit = Check_OS_Bit()
#				Dir.chdir(osbit)
				puts("Install driver now")
				`dpinst /lm /se /sw /f`
				rc = $?
				if rc.exitstatus == 1
					puts("Install succeeded")
					`tasklist | find /i "CloseSecurityWindow.exe"`
					Write_Log(drivername)
				else
					puts("Install Failed")
					exit(rc.exitstatus)
				end
			else
				exit(rc)
			end
		else
			puts (drivername + " has already installed,skipping...")
			exit(0)
		end
else 
	exit(0)
end
