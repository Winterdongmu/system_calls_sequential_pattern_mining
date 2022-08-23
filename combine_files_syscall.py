import pandas as pd
import math
path = "G:\project\lisa_data\classify_based_on_files.csv"
path2 = "G:\project\lisa_data\classify_based_on_syscall.csv"
path3 = "G:\project\lisa_data\collect_system_calls.csv"

def convert_list(path):
       df_target = pd.read_csv(path, index_col=0)
       column_name = df_target.columns.values

       new_list = []
       for i in column_name:
              list_of_single_column = df_target[i].tolist()
              list_of_single_column.insert(0,i)
              newlist = [x for x in list_of_single_column if type(x) == str]
              # print(newlist)
              new_list.append(newlist)
       return new_list

file_list = convert_list(path)

for i in file_list:
       for j in range(len(i)):

              i[j] = i[j].replace('.out_files.csv', '.out_converted.csv')




df_target = pd.read_csv(path3, index_col=0)
colume_name = df_target.columns.values
share_dictionary = {}
specific_files_dict = {}
for i in file_list:
       print("i:",i)

       if len(i) > 1:
              list_number = list(range(len(i)))
              list_number.pop()
              list_number2 = list(range(len(i)))

              for j in list_number:
                     df_new = df_target.loc[i[j]]
                     list_number2.pop(0)
                     sys_count = 0
                     first_list = []
                     share_file_store = []
                     share_file_store_index = 0


                     for colume_index in colume_name:
                            if df_new[colume_index] == 1:
                                   sys_count += 1

                     for jj in list_number2:
                            df_new_2 = df_target.loc[i[jj]]
                            second_sys_count = 0
                            share_count = 0
                            share_file_store_tmp = []

                            for colume_index in colume_name:
                                   if df_new_2[colume_index] == 1:
                                          second_sys_count += 1


                            for colume_index in colume_name:
                                   if df_new[colume_index] == 1 and df_new[colume_index] == df_new_2[colume_index]:
                                          share_count += 1
                                          share_file_store_tmp.append(colume_index)

                            if share_count / sys_count >= 0.7 and second_sys_count / sys_count < 2:
                                   first_list.append(i[jj])
                                   i.pop(jj)
                                   share_file_store.append([])
                                   share_file_store[share_file_store_index] = share_file_store_tmp
                                   share_file_store_index += 1
                                   list_number.pop()
                                   list_number2.pop()
                     share = []
                     if len(share_file_store) != 0:
                            share = share_file_store[0]
                            for k in range(len(share_file_store)):
                                   share = set(share) & set(share_file_store[k])

                     share_dictionary[i[j]] = first_list
                     print('i[j]:',i[j])
                     print('first:',first_list)
                     print('\n')
                     specific_files_dict[i[j]] = share
                     # print(df_new_2["open"])
# syscall_list = convert_list(path2)
df = pd.DataFrame.from_dict(share_dictionary, orient='index')
df.T.to_csv('classify_based_combined.csv')

df2 = pd.DataFrame.from_dict(specific_files_dict, orient='index')
df2.T.to_csv('classify_based_combined_specific.csv')
# print(file_list)

# # print(syscall_list)
# Aug 03 11:37:33 ubuntu falco[167240]: {"output":"2022-08-03T15:37:33.637598824+0000: Error Packet socket was created in a container socket_info=domain=1 type=526337 proto=0  evt.info:domain=1 type=526337 proto=0  proc.args=-xmf - -C /home/test connection=<NA> container_id=d4bbd01a5615 user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = domain=1 type=526337 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA>          fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T15:37:33.637598824Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"domain=1 type=526337 proto=0 ","evt.info":"domain=1 type=526337 proto=0 ","evt.time.iso8601":1659541053637598824,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 11:37:33 ubuntu falco[167240]: {"output":"2022-08-03T15:37:33.637605734+0000: Error Packet socket was created in a container socket_info=fd=3(<u>)                     evt.info:fd=3(<u>)                     proc.args=-xmf - -C /home/test connection=     container_id=d4bbd01a5615 user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = fd=3(<u>)                     fd.num=3  fd.type=unix fd.l4proto=<NA> fd.sockfamily=unix fd.containername=d4bbd01a5615: fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T15:37:33.637605734Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"fd=3(<u>) ","evt.info":"fd=3(<u>) ","evt.time.iso8601":1659541053637605734,"evt.type":"socket","fd.cip":null,"fd.containername":"d4bbd01a5615:","fd.l4proto":"<NA>","fd.lip":null,"fd.name":"","fd.num":3,"fd.rip":null,"fd.sip":null,"fd.sockfamily":"unix","fd.type":"unix","proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
#
#
# Aug 03 11:43:34 ubuntu falco[167240]: {"output":"2022-08-03T15:43:34.881450386+0000: Error Packet socket was created in a container socket_info=domain=2 type=526338 proto=0  evt.info:domain=2 type=526338 proto=0  proc.args=                     connection=<NA> container_id=d4bbd01a5615 user=root user_loginuid=-1  command=1e48915f40bfdd7          event=socket evt.args = domain=2 type=526338 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA>          fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T15:43:34.881450386Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"domain=2 type=526338 proto=0 ","evt.info":"domain=2 type=526338 proto=0 ","evt.time.iso8601":1659541414881450386,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"                                                          ","proc.cmdline":"1e48915f40bfdd7                                                           ","user.loginuid":-1,"user.name":"root"}}
# Aug 03 11:43:34 ubuntu falco[167240]: {"output":"2022-08-03T15:43:34.881608488+0000: Error Packet socket was created in a container socket_info=fd=10(<4>)                    evt.info:fd=10(<4>)                    proc.args=                     connection=     container_id=d4bbd01a5615 user=root user_loginuid=-1  command=1e48915f40bfdd7          event=socket evt.args = fd=10(<4>)                    fd.num=10 fd.type=ipv4 fd.l4proto=<NA> fd.sockfamily=ip   fd.containername=d4bbd01a5615: fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T15:43:34.881608488Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"fd=10(<4>) ","evt.info":"fd=10(<4>) ","evt.time.iso8601":1659541414881608488,"evt.type":"socket","fd.cip":null,"fd.containername":"d4bbd01a5615:","fd.l4proto":"<NA>","fd.lip":null,"fd.name":"","fd.num":10,"fd.rip":null,"fd.sip":null,"fd.sockfamily":"ip","fd.type":"ipv4","proc.args":"                                                          ","proc.cmdline":"1e48915f40bfdd7                                                           ","user.loginuid":-1,"user.name":"root"}}
#
#
# Aug 03 12:02:27 ubuntu falco[167240]: {"output":"2022-08-03T16:02:27.845579873+0000: Error Is trying to send data to some places socket_info=res=48 data=.............bucsa.winscp.top.cluster.local.....  evt.info:res=48 data=.............bucsa.winscp.top.cluster.local.....  proc.args=                                                           connection=192.168.235.152:53570->10.96.0.10:53 container_id=d4bbd01a5615 user=<NA> user_loginuid=-1  command=1e48915f40bfdd7                                                            event=sendto evt.args = res=48 data=.............bucsa.winscp.top.cluster.local.....  fd.num=10 fd.type=ipv4 fd.l4proto=udp fd.sockfamily=ip fd.containername=d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53 fd.ips=192.168.235.152 10.96.0.10 192.168.235.152 10.96.0.10","priority":"Error","rule":"sendto or connect","source":"syscall","tags":["container","users"],"time":"2022-08-03T16:02:27.845579873Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.info":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.time.iso8601":1659542547845579873,"evt.type":"sendto","fd.cip":"192.168.235.152","fd.containername":"d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53","fd.l4proto":"udp","fd.lip":"192.168.235.152","fd.name":"192.168.235.152:53570->10.96.0.10:53","fd.num":10,"fd.rip":"10.96.0.10","fd.sip":"10.96.0.10","fd.sockfamily":"ip","fd.type":"ipv4","proc.args":"                                                          ","proc.cmdline":"1e48915f40bfdd7                                                           ","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 12:02:27 ubuntu falco[167240]: {"output":"2022-08-03T16:02:27.845565289+0000: Error Is trying to send data to some places socket_info=res=48 data=.............bucsa.winscp.top.cluster.local.....  evt.info:res=48 data=.............bucsa.winscp.top.cluster.local.....  proc.args=                                                           connection=192.168.235.152:53570->10.96.0.10:53 container_id=d4bbd01a5615 user=<NA> user_loginuid=-1  command=1e48915f40bfdd7                                                            event=sendto evt.args = res=48 data=.............bucsa.winscp.top.cluster.local.....  fd.num=10 fd.type=ipv4 fd.l4proto=udp fd.sockfamily=ip fd.containername=d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53 fd.ips=192.168.235.152 10.96.0.10 192.168.235.152 10.96.0.10","priority":"Error","rule":"sendto or connect","source":"syscall","tags":["container","users"],"time":"2022-08-03T16:02:27.845565289Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.info":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.time.iso8601":1659542547845565289,"evt.type":"sendto","fd.cip":"192.168.235.152","fd.containername":"d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53","fd.l4proto":"udp","fd.lip":"192.168.235.152","fd.name":"192.168.235.152:53570->10.96.0.10:53","fd.num":10,"fd.rip":"10.96.0.10","fd.sip":"10.96.0.10","fd.sockfamily":"ip","fd.type":"ipv4","proc.args":"                                                          ","proc.cmdline":"1e48915f40bfdd7                                                           ","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 12:02:27 ubuntu falco[167240]: {"output":"2022-08-03T16:02:27.845579873+0000: Error Is trying to send data to some places socket_info=res=48 data=.............bucsa.winscp.top.cluster.local.....  evt.info:res=48 data=.............bucsa.winscp.top.cluster.local.....  proc.args=                                                           connection=192.168.235.152:53570->10.96.0.10:53 container_id=d4bbd01a5615 user=<NA> user_loginuid=-1  command=1e48915f40bfdd7                                                            event=sendto evt.args = res=48 data=.............bucsa.winscp.top.cluster.local.....  fd.num=10 fd.type=ipv4 fd.l4proto=udp fd.sockfamily=ip fd.containername=d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53 fd.ips=192.168.235.152 10.96.0.10 192.168.235.152 10.96.0.10","priority":"Error","rule":"sendto or connect","source":"syscall","tags":["container","users"],"time":"2022-08-03T16:02:27.845579873Z", "output_fields": {"container.id":"d4bbd01a5615","evt.args":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.info":"res=48 data=.............bucsa.winscp.top.cluster.local..... ","evt.time.iso8601":1659542547845579873,"evt.type":"sendto","fd.cip":"192.168.235.152","fd.containername":"d4bbd01a5615:192.168.235.152:53570->10.96.0.10:53","fd.l4proto":"udp","fd.lip":"192.168.235.152","fd.name":"192.168.235.152:53570->10.96.0.10:53","fd.num":10,"fd.rip":"10.96.0.10","fd.sip":"10.96.0.10","fd.sockfamily":"ip","fd.type":"ipv4","proc.args":"                                                          ","proc.cmdline":"1e48915f40bfdd7                                                           ","user.loginuid":-1,"user.name":"<NA>"}}

# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:14:50.071901340+0000: Error pthread library opened. (container_id=c8be72b5babd user=root user_loginuid=-1 command=mkdir test filename=<NA> name=/etc/ld.so.cache mode=0 event=openat)","priority":"Error","rule":"thread related library read","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:14:50.071901340Z", "output_fields": {"container.id":"c8be72b5babd","evt.arg.filename":null,"evt.arg.mode":"0","evt.arg.name":"/etc/ld.so.cache","evt.time.iso8601":1659554090071901340,"evt.type":"openat","proc.cmdline":"mkdir test","user.loginuid":-1,"user.name":"root"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:22.953968068+0000: Error pthread library opened. (container_id=c8be72b5babd user=<NA> user_loginuid=-1 command=test -d /home/test filename=<NA> name=/etc/ld.so.cache mode=0 event=openat)","priority":"Error","rule":"thread related library read","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:22.953968068Z", "output_fields": {"container.id":"c8be72b5babd","evt.arg.filename":null,"evt.arg.mode":"0","evt.arg.name":"/etc/ld.so.cache","evt.time.iso8601":1659554122953968068,"evt.type":"openat","proc.cmdline":"test -d /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:23.124244863+0000: Error pthread library opened. (container_id=c8be72b5babd user=<NA> user_loginuid=-1 command=tar -xmf - -C /home/test filename=<NA> name=/etc/ld.so.cache mode=0 event=openat)","priority":"Error","rule":"thread related library read","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:23.124244863Z", "output_fields": {"container.id":"c8be72b5babd","evt.arg.filename":null,"evt.arg.mode":"0","evt.arg.name":"/etc/ld.so.cache","evt.time.iso8601":1659554123124244863,"evt.type":"openat","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:23.127359315+0000: Error Packet socket was created in a container socket_info=domain=1 type=526337 proto=0  evt.info:domain=1 type=526337 proto=0  proc.args=-xmf - -C /home/test connection=<NA> container_id=c8be72b5babd user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = domain=1 type=526337 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA> fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:23.127359315Z", "output_fields": {"container.id":"c8be72b5babd","evt.args":"domain=1 type=526337 proto=0 ","evt.info":"domain=1 type=526337 proto=0 ","evt.time.iso8601":1659554123127359315,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:23.127381836+0000: Error Packet socket was created in a container socket_info=domain=1 type=526337 proto=0  evt.info:domain=1 type=526337 proto=0  proc.args=-xmf - -C /home/test connection=<NA> container_id=c8be72b5babd user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = domain=1 type=526337 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA> fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:23.127381836Z", "output_fields": {"container.id":"c8be72b5babd","evt.args":"domain=1 type=526337 proto=0 ","evt.info":"domain=1 type=526337 proto=0 ","evt.time.iso8601":1659554123127381836,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:23.127441642+0000: Error Packet socket was created in a container socket_info=domain=1 type=526337 proto=0  evt.info:domain=1 type=526337 proto=0  proc.args=-xmf - -C /home/test connection=<NA> container_id=c8be72b5babd user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = domain=1 type=526337 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA> fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:23.127441642Z", "output_fields": {"container.id":"c8be72b5babd","evt.args":"domain=1 type=526337 proto=0 ","evt.info":"domain=1 type=526337 proto=0 ","evt.time.iso8601":1659554123127441642,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
# Aug 03 15:15:23 ubuntu falco[167240]: {"output":"2022-08-03T19:15:23.127452592+0000: Error Packet socket was created in a container socket_info=domain=1 type=526337 proto=0  evt.info:domain=1 type=526337 proto=0  proc.args=-xmf - -C /home/test connection=<NA> container_id=c8be72b5babd user=<NA> user_loginuid=-1  command=tar -xmf - -C /home/test event=socket evt.args = domain=1 type=526337 proto=0  fd.num=-1 fd.type=<NA> fd.l4proto=<NA> fd.sockfamily=<NA> fd.containername=<NA> fd.ips=<NA> <NA> <NA> <NA>","priority":"Error","rule":"socket created","source":"syscall","tags":["container","users"],"time":"2022-08-03T19:15:23.127452592Z", "output_fields": {"container.id":"c8be72b5babd","evt.args":"domain=1 type=526337 proto=0 ","evt.info":"domain=1 type=526337 proto=0 ","evt.time.iso8601":1659554123127452592,"evt.type":"socket","fd.cip":null,"fd.containername":null,"fd.l4proto":null,"fd.lip":null,"fd.name":null,"fd.num":-1,"fd.rip":null,"fd.sip":null,"fd.sockfamily":null,"fd.type":null,"proc.args":"-xmf - -C /home/test","proc.cmdline":"tar -xmf - -C /home/test","user.loginuid":-1,"user.name":"<NA>"}}
