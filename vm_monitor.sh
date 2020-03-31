calculate_RAM () {
        node_memory_MemTotal=$(curl -s http://$1:9100/metrics | grep node_memory_MemTotal | grep -v '#'| awk '{print $2*0.000001}')
        node_memory_MemFree=$(curl -s http://$1:9100/metrics | grep node_memory_MemFree | grep -v "#"| awk '{print $2*0.000001}')
        node_memory_Buffers=$(curl -s http://$1:9100/metrics | grep node_memory_Buffers | grep -v "#"| awk '{print $2*0.000001}')
        node_memory_Cached=$(curl -s http://$1:9100/metrics | grep node_memory_Cached | grep -v "#"| awk '{print $2*0.000001}')
        node_memory_Free=$(awk "BEGIN {printf(($node_memory_MemTotal - $node_memory_MemFree - $node_memory_Buffers - $node_memory_Cached) / $node_memory_MemTotal) * 100}")
	echo $node_memory_Free
}

calculate_uptime () {
	node_time_days=$(curl -s http://$1:9100/metrics | grep -i node_time_seconds | grep -v "#" | awk '{print $2/60/60/24}')
	node_boot_time_days=$(curl -s http://$1:9100/metrics | grep -i node_boot_time_seconds | grep -v "#" | awk '{print $2/60/60/24}')
	node_up_time=$(awk "BEGIN {printf($node_time_days - $node_boot_time_days)}")
	echo $node_up_time
}

for i in $(virsh net-dhcp-leases default | grep ipv4 | awk '{print $5}' | sed 's/\/24//g')
do
	echo Date: $(date) >> /opt/data/$i.data
	curl -s http://$i:9100/metrics | grep node_load15 | grep -v "#" | awk '{print "CPU Average: "$2 " #node cpu load 15 minutes average"}' >> /opt/data/$i.data
	curl -s http://$i:9100/metrics | grep 'node_network_transmit_packets_total{device="eth0"}' | awk '{print "Network transmit: "$2 " #node_network_transmit_packets_total"}' >> /opt/data/$i.data
	curl -s http://$i:9100/metrics | grep 'node_network_receive_packets_total{device="eth0"}' | awk '{print "Network receive: "$2 " #node_network_receive_packets_total"}' >> /opt/data/$i.data
	echo Used RAM: $(calculate_RAM "$i") \#Used RAM>> /opt/data/$i.data
	echo Uptime: $(calculate_uptime "$i") \#In days >> /opt/data/$i.data
	echo Kernel version: $(curl -s http://$i:9100/metrics | grep -i node_uname_info | grep release | cut -d , -f 4| cut -d = -f 2 | sed 's/"//g') >> /opt/data/$i.data
done
