#!/usr/bin/python
import requests
import json
import pprint
#cdna url
#https://computerdna.monitoringclient.com/v2.5/
#my api key
#yKuXkDN4-SU2PE0BtK6qlY1UjcqfUX-GoIhVnw
#&group_id=g_1d6dda5f2b used to only list computers from specific groups
url = "https://mysubdomain.monitoringclient.com/v2.5/computers/?api_key=mMYGREATAPIKEYgroup_id=GROUPID&expand[]=plugin_results"
r = requests.get(url)
current_operating_system = '0.0.0'
# Store API response in a variable.
response_dict = r.json()


for iNumber in range(0,10):
    
    c_id = response_dict[iNumber]['client_id']
    c_name = response_dict[iNumber]['computer_name']
    l_report = response_dict[iNumber]['last_report']
    group_member = response_dict[iNumber]['group']
    l_user = response_dict[iNumber]['last_user']
    s_number = response_dict[iNumber]['serial_number']
    r_email = response_dict[iNumber]['reference_email']
    o_version = response_dict[iNumber]['os_version']
    m_name = response_dict[iNumber]['model_name']
    l_report = response_dict[iNumber]['last_report']
    e_purchase = response_dict[iNumber]['estimated_purchase_date']
    r_installed = response_dict[iNumber]['ram_installed']
    max_os = response_dict[iNumber]['os_version_number_max']
    r_intalled = response_dict[iNumber]['ram_installed']
    r_max = response_dict[iNumber]['ram_max_apple']
    c_desc = response_dict[iNumber]['config_description']
    proc = response_dict[iNumber]['processor']
    up_time = response_dict[iNumber]['current_uptime']
    a_care = response_dict[iNumber]['applecare_eligibility']
    w_status = response_dict[iNumber]['warranty_status']
    b_volume = response_dict[iNumber]['boot_volume_capacity']
    b_used = response_dict[iNumber]['boot_volume_usage']
    b_percent = response_dict[iNumber]['boot_volume_usage_percent']
    plug = response_dict[iNumber]['plugin_results']
  

    #print
    print("Machine Model {} with the configuration: {}".format (m_name, c_desc))
    print("\tThe current amount of RAM installed is: {} and the max that your Mac can be upgraded to is: {}".format(r_installed, r_max))
    print("\tProcessor: ", (proc))
    print("\tEstimated Purchase Date:", (e_purchase))
    print("\tThe computer name is: {} and the last user is: {}".format(c_name, l_user))
    print("\tThe last time your machine checked in was: ", (l_report))
    print("\tMember of Group: ", (group_member))
    print("\tSerial Number :", (s_number))
    print("\tReference Email :", (r_email))
    if max_os == (current_operating_system): 

        print("\tCurrent OS is {} and you can run the latest OS.".format(o_version))
    else:
        print("\tCurrent OS is {} and the max version is {}".format(o_version, max_os))
    print("\tYour computer has been on for: ", (up_time))
    print("\tApple Care Status: {} and the status of the warranty is: {}".format(a_care, w_status))
    print("\tYour boot volume has a capacity of: {}, you have used:{} or {}% of your total capacity".format(b_volume, b_used, b_percent))
    print("\tPlugin Results: ", (plug))
    print(plug.list())
    print()