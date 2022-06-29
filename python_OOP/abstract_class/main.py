from ftemployee import FullTimeEmployee
from hemployee import HourlyEmployee
from payroll import Payroll


payroll = Payroll()


payroll.add(FullTimeEmployee("Rick", "Biswas", 60000))
payroll.add(FullTimeEmployee("ayush", "Biswas", 20000))
payroll.add(HourlyEmployee("roni", "sarkar", 90, 60))
payroll.add(HourlyEmployee("pritam", "sarkar", 100, 30))
payroll.add(HourlyEmployee("dibbo", "sarkar", 20, 50))


payroll.print_em()
