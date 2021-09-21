# Network Management Tool

import os
from rich.console import Console

console = Console()

def menu():
	interface = os.popen("ls /sys/class/net").read() # gets the interface details
	print("-----------Menu for interface------------")
	val = interface.split("\n")[-7:-1]
	count = 1
	for i in val:
		console.print(f"\t{count}.{i}",style="bold green")
		count += 1


def assign_ip():
	menu()
	ip = input("Enter the ip address to add :")
	inter_name = input("Enter the interface name from above menu list :")
	cmd =f"sudo ip address add {ip} dev {inter_name}" # assigning ip address
	ip_assign = os.popen(cmd).read()
	print("...................Assigning IP...............................")
	print(os.popen(f"ip -4 a show {inter_name}").read()) # showing ip address
	console.print("\tSuccessfully Added the IP address",style="bold blue") 	

def del_ip():
	menu()
	ip = input("Enter the ip address to delete :")
	inter_name = input("Enter the interface name from above menu list :")
	cmd = f"sudo ip address del {ip} dev {inter_name}" # deleting ip address
	del_ip = os.popen(cmd).read()
	print("....................Deleting IP.................................")
	print(os.popen(f"ip -4 a show {inter_name}").read()) # showing ip address
	console.print("\tSuccessfully Deleted the IP address",style="bold red") 

def display_ip():
	menu()
	inter_name = input("Enter the interface name from above menu list :")
	cmd = f"sudo ip -4 a show {inter_name}" # showing ip address
	dis = os.popen(cmd).read()
	print("..................Displaying IP.......................")
	console.print(dis,style="bold blue")
	
def display_interface():
	cmd = f"sudo ip l"
	dis_inter = os.popen(cmd).read() # showing interfaces
	print(".......................Displaying interface....................")
	console.print(dis_inter,style="bold blue")

def conf_route():
	menu()
	ip = input("Enter the ip address to add :")
	inter_name = input("Enter the interface name :")
	cmd = f"sudo ip r add 10.2.3.0/24 via {ip} dev {inter_name}" # addind new route
	print("....................Adding Routing..........................")
	print(os.popen("ip r").read()) 
	console.print("\tSuccessfully added the routing",style="bold blue")
	
def turn_On_Off_interface():
	while True:
		menu()
		print("\t.............Menu for turn/off interface.............")
		console.print("\t1.Turn on interface",style="bold blue")
		console.print("\t2.Turn off interface",style="bold blue")
		console.print("\t3.Exit",style="bold blue")
		ch = int(input("\tEnter the choice"))
		if ch == 1:
			inter_name = input("\tEnter the interface name from the above menu list :")
			cmd = f"sudo ip link set dev {inter_name} up" # turn on interface
			on = os.popen(cmd).read()
			print("................Turn on interface................")
			print(os.popen("ip a").read())
			console.print("\tSuccessfully turned on the interface",style="bold blue")
		
		elif ch == 2:
			inter_name = input("Enter the interface name :")
			cmd = f"sudo ip link set dev {inter_name} down" # turn off interface
			down = os.popen(cmd).read()
			print(".................Turn off interface........................")
			print(os.popen("ip a").read())
			console.print("\tSuccessfully turned off the interface",style="bold red")
		elif ch == 3:
			break
		else:
			console.print("\tInvalid choice",style="bold red")

def add_arp_entry():
	menu()
	inter_name = input("Enter the interface name :")
	cmd =f"sudo ip n add 192.168.1.200 lladdr 00:45:78:52:ed:55 dev {inter_name} nud permanent" # add arp entry
	arp = os.popen(cmd).read()
	print(".................Adding ARP entry.......................")
	print(os.popen("ip n show").read())
	console.print("\tSuccesffuly added the arp entry",style="bold blue")

def delete_arp_entry():
	menu()
	inter_name = input("Enter the interface name :")
	cmd =f"sudo ip n flush 192.168.1.200 dev {inter_name} nud permanent" # flush arp entry
	arp = os.popen(cmd).read()
	print("........................Deleting ARP entry....................")
	print(os.popen("ip n show").read())
	console.print("\tSuccessfully deleted the arp entry",style="bold red")

def restart_network():
	cmd = "sudo systemctl status  networking" # restart network service
	re_net = os.popen(cmd).read()
	print(".................Restarting network................")
	console.print(re_net,style="bold blue")

def change_hostname():
	cmd = "sudo hostname shanususanabraham" # change hostname
	change_host = os.popen(cmd).read()
	change_host_det = os.popen("hostnamectl status").read()
	print(".................Changing Host name..............")
	console.print(change_host_det,style="bold blue")

def new_dns_entry():
	dns = os.popen("sudo cat >> /etc/resolv.conf").read() # add new dns server
	print(".................Adding DNS entry................")
	console.print(dns,style="bold blue")	

while True:
	print(".......................Menu.....................")
	console.print("\t1.Assign IP",style="bold blue")
	console.print("\t2.Delete Ip",style="bold blue")
	console.print("\t3.Display Ip",style="bold blue")
	console.print("\t4.Dispaly all interfaces",style="bold blue")
	console.print("\t5.Configure routing",style="bold blue")
	console.print("\t6.Turn On/Off interface",style="bold blue")
	console.print("\t7.Add ARP entry",style="bold blue")
	console.print("\t8.Delete ARP Entry",style="bold blue")
	console.print("\t9.Restart Network",style="bold blue")
	console.print("\t10.Change Hostname",style="bold blue")
	console.print("\t11.Add DNS server entry",style="bold blue")
	console.print("\t12.Exit",style="bold blue")
	choice = int(input("\tEnter your choice"))
	if choice == 1:
		assign_ip()
	elif choice == 2:
		del_ip()
	
	elif choice == 3:
		display_ip()
	elif choice == 4:
		display_interface()
	elif choice == 5:
		conf_route()
	elif choice == 6:
		turn_On_Off_interface()
	elif choice == 7:
		add_arp_entry()
	elif choice == 8:
		delete_arp_entry()
	elif choice == 9:
		restart_network()
	elif choice == 10:
		change_hostname()
	elif choice == 11:
		new_dns_entry()
	elif choice == 12:
		break
	else:
		console.print("\tWrong choice",style="bold red")


