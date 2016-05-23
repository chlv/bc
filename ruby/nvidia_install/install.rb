require 'find'
require 'fileutils'
# install or skip driver
def check_device()
	`C:\\Drvpack64\\Autobot\\utils\\sutconfig`
	flag = 0
	File.open("C:\\Users\\Administrator\\AppData\\Local\\Temp\\config.txt","r") do |c_file|
		while cline = c_file.gets  
			list = cline.split(" ")
			did = list[1]
			vid = list[2]
			File.open("C:\\Users\\Administrator\\AppData\\Local\\Temp\\device.txt","r") do |sut_file|
				while sline = sut_file.gets
					if  did != nil and sline.include?("10DE") and sline.include?(did)
						flag = 1
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
# check if driver installed
def check_driver_installed()
		rc = -1
		if File.exist?('C:\NVIDIA\DisplayDriver')
			puts "Driver has already installed"
			rc = 0
			return rc 
		else
			puts "Driver not installed"
			puts "Unzip driver now.... it will take several minutes"
			return false
		end
end


# get driver name
def get_driver_name()
		driver_name = ""
		Dir.foreach(Dir.pwd) {|x| if x.include? "-" 
										driver_name = x										 
								 end}

		return driver_name
end

# unzip *.exe  and install driver
def install_driver(driver_name)
	rc = -1
	`#{driver_name} /s /n`
	rc = $?
	if rc.exitstatus == 1
		puts "install OK"
		rc = 0
	else
		puts "install Fail"
		rc = 900
	end
	return rc
end

# get the unzip path
#def get_path(driver_name)
#	name_array = []
#	get driver version
#	name_array = driver_name.split('-')
#	name_version = name_array[0]
#	path = "C:\\NVIDIA\\DisplayDriver\\" + "#{name_version}"
#	puts path
#	Find.find (path) {|f| if (File.basename(f) == "setup.exe")
#								path = f
#							end
#	}
#	path=(path.split("/")).join("\\")
#	return path

#end

# install driver run setup.exe
#def install_driver(path) 
#	rc = -1
#	Dir.chdir(File.dirname(path))
#	puts 'Path is ok,installing driver now...'
#	`#{path} /n /s`
#	rc = $?
#	if rc.success? 
#		puts "Install OK"
#		rc = 0
#		return rc
#	else
#		puts "Install Fail"
#		rc = 900
#		return rc
#	end
#end

if check_device == true
	begin
		rc = -1
		rc = check_driver_installed()
		if rc == false
			rc = install_driver(get_driver_name())
		else
			exit(rc)
		end
	#	if rc != 0
	#		exit
	#	end
	#	path = get_path(get_driver_name())
	#	puts path
	#	rc = install_driver(path)
	#	FileUtils.rm "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\install.rb"
	rescue Exception => e
		puts e.message if e.message != "exit"
	ensure
		# Exit with the install return code
		exit(rc)
	end
else 
	exit(0)
end
