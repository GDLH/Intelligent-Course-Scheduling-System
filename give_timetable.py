import pdb
import copy

#m_teachers：教师类
class teacher:
	#定义姓名，教授课程
	def __init__(self, t_name, t_class_name):
		#str类型
		self.t_name = t_name
		#str类型
		self.t_class_name = t_class_name

#m_teaching_classes：教学班（上课专业）列表
#教学班是一个包含str的列表。如：['计科', '软工', '物联网']

#m_classrooms：教室列表，如['301102', '302203', '田径场']
#用isdigit()来区别是教室还是户外课

#m_courses：课程类
#几个变量的定义：
#class_type定义
#大项活动(节假日)：这些活动的日期安排是固定的。注意：大项活动如果对时间段做出限制，则按天拆分开。
major_activities = 0
#军事(体育)实践课：是公共课程，有学时数限制，会安排教员。此外，单课时的军事(体育)课一般放在每天最后一个课时。
#如果安排了连堂的军事(体育)课，当天应该安排1~2节自习
#实践课由于对体能有要求，会加入对季节的限制。这里通过限制起止日期来限制，并且对其优先排课。
military_sport_class = 1
#公共课：普通的课程。有学时数限制，会安排教员。文化课不允许对上课的起止日期，星期与时间段做出限制
culture_class = 2

#class_quantum_type的定义：无限制为0，连续上两节为1，全天上课为2
free = 0
two_class_hour_continuous = 1
all_day_continuous = 2

#force_quantum_list：
#force_quantum_list为长度4的列表。例：[0,0,0,0]表示这门课安排在下午的两节

#teaching_class_list：将上这门课的教学班名称放入这个列表

class course:
	#定义课程名，课时数，课程类型，是否连堂上课，限制时间段上课，限制上课开始日期，限制上课结束日期，上该门课程的教学班列表，户外课上课的场所
	def __init__(self, c_name, c_class_hours, c_class_type, c_class_quantum_type, c_force_quantum_list, \
		c_force_start_time, c_force_end_time, c_teaching_class_list, c_classroom):
		#课程名，str类型：如：'软工'
		self.c_name = c_name
		#课时数，int类型：如：64
		self.c_class_hours = c_class_hours
		#课程类型，int类型。见上方的定义
		self.c_class_type = c_class_type
		#是否连堂上课，int类型。见上方的定义
		self.c_class_quantum_type = c_class_quantum_type
		#限制时间段上课，列表类型。见上方的定义
		self.c_force_quantum_list = c_force_quantum_list
		#限制上课开始日期、限制上课结束日期，int类型，为8位数字，如：20190101
		#起止日期初始化为学期的开始与结束日期。
		self.c_force_start_time = c_force_start_time
		self.c_force_end_time = c_force_end_time
		#列表类型，如：['计科', '软工', '物联网']
		#c_teaching_class_list初始化为全部专业
		self.c_teaching_class_list = c_teaching_class_list
		self.c_classroom = c_classroom

#计算课表需要引用的函数：
#判断是否为闰年
def is_leap_year(year):
	if (year % 4 == 0):
		if (year % 100 != 0):
			return True
		elif (year % 400 == 0):
			return True
		else:
			return False

#判断某个月的天数
def days_of_month(month, year):
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
		return 31
	elif (month == 2 and is_leap_year(year)):
		return 29
	elif (month == 2 and not is_leap_year(year)):
		return 28
	elif (month == 4 or month == 6 or month == 9 or month == 11):
		return 30
	else:
		return 0

#由8位年月日数字组合拆分出年、月、日
def time_to_date(time):
	return time % 100
def time_to_month(time):
	return (time % 10000) // 100
def time_to_year(time):
	return time // 10000

#计算下一天的8位年月日代码
def time_next_day(time):
	if ((time_to_month(time) == 2 and is_leap_year(time_to_year(time)) and time_to_date(time) == 29)\
		or (time_to_month(time) == 2 and (not is_leap_year(time_to_year(time))) and time_to_date(time) == 28)):
		return time_to_year(time) * 10000 + 301
	elif (time_to_month(time) == 12 and time_to_date(time) == 31):
		return (time_to_year(time) + 1) * 10000 + 101
	elif ((time_to_month(time) == 1 or time_to_month(time) == 3 or time_to_month(time) == 5 or time_to_month(time) == 7\
		or time_to_month(time) == 8 or time_to_month(time) == 10) and time_to_date(time) == 31):
		return time_to_year(time) * 10000 + (time_to_month(time) + 1) * 100 + 1
	elif ((time_to_month(time) == 4 or time_to_month(time) == 6 or time_to_month(time) == 9 or time_to_month(time) == 11)\
		and time_to_date(time) == 30):
		return time_to_year(time) * 10000 + (time_to_month(time) + 1) * 100 + 1
	else:
		return time + 1

#计算上一天的8位年月日代码
def time_before_day(time):
	if (time_to_month(time) == 3 and time_to_date(time) == 1):
		if (is_leap_year(time_to_year(time))):
			return time_to_year(time) * 10000 + 229
		else:
			return time_to_year(time) * 10000 + 228
	elif (time_to_month(time) == 1 and time_to_date(time) == 1):
		return (time_to_year(time) - 1) * 10000 + 1231
	elif ((time_to_month(time) == 3 or time_to_month(time) == 5 or time_to_month(time) == 7 or time_to_month(time) == 8\
		or time_to_month(time) == 10 or time_to_month(time) == 12) and time_to_date(time) == 1):
		return time_to_year(time) * 10000 + (time_to_month(time) - 1) * 100 + 30
	elif ((time_to_month(time) == 4 or time_to_month(time) == 6 or time_to_month(time) == 9 or time_to_month(time) == 11)\
		and time_to_date(time) == 1):
		return time_to_year(time) * 10000 + (time_to_month(time) - 1) * 100 + 31
	else:
		return time - 1

#计算下一天为星期几
def day_next_day(day):
	if (day == 7):
		day_tmp = 1
	else:
		day_tmp = day + 1
	return day_tmp

#计算当天是否在一个时间段内
def if_between(time, time_start, time_end):
	if ((time >= time_start) and (time <= time_end)):
		return True
	else:
		return False 

#计算学期时长
def sum_of_days(start_time, end_time, start_day):
	#分解起止日期的8位代码，便于排课
	start_date = time_to_date(start_time)
	start_month = time_to_month(start_time)
	start_year = time_to_year(start_time)
	end_date = time_to_date(end_time)
	end_month = time_to_month(end_time)
	end_year = time_to_year(end_time)

	if (end_year == start_year):
		if (end_month == start_month):
			num_of_days = end_time - start_time + 1
		else:
			num_of_days = days_of_month(start_month, start_year) - start_date + 1 + end_date
			for i in range(start_month + 1, end_month):
				num_of_days = num_of_days + days_of_month(i, start_year)
	else:
		num_of_days = days_of_month(start_month, start_year) - start_date + 1 + end_date
		for i in range(start_month + 1, 13):
			num_of_days = num_of_days + days_of_month(i, start_year)
		for i in range(1, end_month):
			num_of_days = num_of_days + days_of_month(i, end_year)
		for i in range(start_year + 1, end_year):
			if (is_leap_year(i)):
				num_of_days = num_of_days + 366
			else:
				num_of_days = num_of_days + 365

	return num_of_days

#计算周平均学时
def average_class_hours_per_week(m_courses, num_of_days):
	hours = 0
	for m_course in m_courses:
		hours = hours + m_course.c_class_hours
	average = hours * 7 // num_of_days
	return average

#计算当天已安排课程数
def day_class_hours_committed(dic):
	courses_num = 0
	for i in range(1, 5):
		#这里是看是否有活动或课程安排，所以拿课程名作为检测key
		if (dic[i]['课程名'] != 0):
			courses_num = courses_num + 1
	return courses_num

#计算当周已安排课程数
def week_class_hours_committed(dic, time):
	courses_num = 0
	#当天是星期几
	day = dic[time]['星期']
	day_tmp1 = day
	day_tmp2 = day_next_day(day)
	time_tmp = time
	while (day_tmp1 >= 1):
		for i in range(1, 5):
			#这里用来平均学时，所以拿教室作为key
			if (dic[time_tmp][i]['教师'] != 0):
				courses_num = courses_num + 1
		time_tmp = time_before_day(time_tmp)
		day_tmp1 = day_tmp1 - 1
	if (day_tmp2 != 1):
		while (day_next_day(day_tmp2) < 2):
			for i in range(1, 5):
				if (dic[time_tmp][i]['教师'] != 0):
					courses_num = courses_num + 1
			time_tmp = time_next_day(time_tmp)
			day_tmp2 = day_next_day(day_tmp2)

	return courses_num

#计算周平均学时
def average_class_hours_per_week(m_courses, num_of_days):
	hours = 0
	for m_course in m_courses:
		hours = hours + m_course.c_class_hours
	average = hours * 7 // num_of_days
	return average

#用于获得对课程列表排序的key
def take_class_type(course):
	return course.c_class_type


'''
def cal(开始时间20190901、结束时间20200117，开始星期7，教师列表['xxx','xxx']，课程名字列表['xxx','xxx']，专业列表，课时列表，课程类型列表，单次课时列表，
       开始上课时间20190901，结束上课时间20200117，上课专业列表[('计算机科学与技术')] ，上课地点‘障碍场’)
class course:
	#定义课程名，课时数，课程类型，是否连堂上课，限制时间段上课，限制上课开始日期，限制上课结束日期，上该门课程的教学班列表，户外课上课的场所
	def __init__(self, c_name, c_class_hours, c_class_type, c_class_quantum_type, c_force_quantum_list, \
		c_force_start_time, c_force_end_time, c_teaching_class_list, c_classroom):

#计算出具有全部信息的课表
#变量意义: 课程起止时间、课程起始为星期几、教师列表、教学班列表、教室列表、课程列表
#def all_information_timetable(start_time, end_time, start_day, m_teachers, m_teaching_classes, m_classrooms, courses):
'''
def cal(start_time, end_time, start_day, teachers, courses, m_teaching_classes, class_hours_list, class_type_list, \
	class_hour_type_list, start_time_list, end_time_list, classes_list, classroom_type_list):

	ts = []
	cs = []
	for i in range(0, len(teachers)):
		t = teacher(teachers[i], courses[i])
		ts.append(t)
		c = course(courses[i], class_hours_list[i], class_type_list[i], class_hour_type_list[i], [0,0,0,0], \
			start_time_list[i], end_time_list[i], classes_list[i], classroom_type_list[i])
		cs.append(c)

	m_teachers = copy.deepcopy(ts)
	courses0 = copy.deepcopy(cs)
	m_classrooms = ['301101', '301102', '301103', '301201', '301202', '301203', '301301', '301302', '301303'] 

	m_courses = sorted(courses0, key = take_class_type)
	#两个变量排序？

	timetable_all = {}
	timetable_tmp = {}
	time_tmp = start_time
	day_tmp = start_day
	avg_courses_week = average_class_hours_per_week(m_courses, sum_of_days(start_time, end_time, start_day))

	#生成空白课程表。0表示空白数据
	for m_teaching_class in m_teaching_classes:
		while(time_tmp <= end_time):
			tmp = {}
			tmp['星期'] = day_tmp
			for i in range(1, 5):
				tmp_tmp = {}
				tmp_tmp['课程名'] = 0
				tmp_tmp['教师'] = 0
				tmp_tmp['教室'] = 0
				tmp[i] = copy.deepcopy(tmp_tmp)
				del tmp_tmp
			timetable_tmp[time_tmp] = copy.deepcopy(tmp)
			del tmp
			time_tmp = time_next_day(time_tmp)
			day_tmp = day_next_day(day_tmp)
		timetable_all[m_teaching_class] = copy.deepcopy(timetable_tmp)

	#生成空白教室占用列表。0表示未占用，1表示已占用
	classrooms_occupy_list = {}
	classrooms_occupy_list_day = {}
	time_tmp = start_time
	for m_classroom in m_classrooms:
		while (time_tmp <= end_time):
			classrooms_occupy_list_day[time_tmp] = [0, 0, 0, 0]
			time_tmp = time_next_day(time_tmp)
		classrooms_occupy_list[m_classroom] = classrooms_occupy_list_day
	#生成空白教师占用列表。0表示未占用，1表示已占用
	teachers_occupy_list = {}
	teachers_occupy_list_day = {}
	time_tmp = start_time
	for m_teacher in m_teachers:
		while (time_tmp <= end_time):
			teachers_occupy_list_day[time_tmp] = [0, 0, 0, 0]
			time_tmp = time_next_day(time_tmp)
		teachers_occupy_list[m_teacher.t_name] = teachers_occupy_list_day

	for m_course in m_courses:
		for m_teaching_class in m_course.c_teaching_class_list:
			time_tmp_timetable = {}
			time_tmp_timetable['课程名'] = 0
			time_tmp_timetable['教师'] = 0
			time_tmp_timetable['教室'] = 0
			time_tmp_timetable['节次'] = 0
			time_tmp = m_course.c_force_start_time
			#设计一个判断器检查课程的学时要求, 满足学时数则停止排课
			class_hours_tmp = m_course.c_class_hours
			#如果这个专业不学这门课程，跳过
			#m_course.c_teaching_class_list的初始化：不做限制时为全部专业
			flag_tc = 0
			for i in m_course.c_teaching_class_list:
				if (i == m_teaching_class):
					flag_tc = 1
					break
			if (not flag_tc):
				time_tmp = time_next_day(time_tmp)
				continue
			#print('OK0')
			time_tmp_timetable['课程名'] = m_course.c_name
			#先安排大项活动
			'''
			#杀掉的功能
			if (m_course.c_class_type == major_activities):
				while(time_tmp <= m_course.c_force_end_time):
					for i in range(1, 5):
						if (m_course.c_force_quantum_list[i - 1]):
							timetable_all[m_teaching_class][time_tmp][i]['课程名'] = m_course.c_name
					time_tmp = time_next_day(time_tmp)
			'''
			if (m_course.c_class_type == major_activities):
				while(time_tmp <= m_course.c_force_end_time):
					for i in range(1, 5):
						timetable_all[m_teaching_class][time_tmp][i]['课程名'] = m_course.c_name
					time_tmp = time_next_day(time_tmp)
			#安排课程。先让排课满足软约束条件，允许有排不出来的课时
			#注意课程列表是按照课程类型排序过的
			#elif (m_course.c_class_type == military_sport_class):
			else:
				#软约束是否成功的标志
				#if_success = 0
				while(time_tmp <= m_course.c_force_end_time):
					#不能满足约束条件则continue
					#0.1 学时数还够
					#print(class_hours_tmp)
					#pdb.set_trace()
					if (class_hours_tmp <= 0):
						break
					#0.2 当天不是周六或周日
					if (timetable_all[m_teaching_class][time_tmp]['星期'] > 5):
						time_tmp = time_next_day(time_tmp)
						continue
					#print('OK0.1')
					#pdb.set_trace()
					#1 当天有足够的课时
					#1.1 非连堂课的处理
					flag_noon = 0
					if (m_course.c_class_quantum_type <= 0):
						if (day_class_hours_committed(timetable_all[m_teaching_class][time_tmp]) >= 4):
							time_tmp = time_next_day(time_tmp)
							continue
					#1.2 连堂课的处理
					elif (m_course.c_class_quantum_type == 1):
						i = 1
						if (timetable_all[m_teaching_class][time_tmp][i]['课程名'] != 0 or \
							timetable_all[m_teaching_class][time_tmp][i + 1]['课程名']):
							flag_noon = flag_noon + 1
						i = i + 2
						if (timetable_all[m_teaching_class][time_tmp][i]['课程名'] != 0 or \
							timetable_all[m_teaching_class][time_tmp][i + 1]['课程名']):
							flag_noon = flag_noon + 2
						if (flag_noon > 2):
							time_tmp = time_next_day(time_tmp)
							continue
					#1.3 全天课的处理
					else:
						flag = 0
						for i in range(1, 5):
							if (timetable_all[m_teaching_class][time_tmp][i]['课程名'] != 0):
								flag = 1
								break
						if (flag):
							time_tmp = time_next_day(time_tmp)
							continue
					#print('OK1')
					#pdb.set_trace()
					time_tmp_timetable['课程名'] = m_course.c_name

					if (m_course.c_class_type != military_sport_class):
						#2 处理教室约束
						#注意：军事(体育)类课程是不占用教室的，所以可以跳过这个约束
						if (m_course.c_class_quantum_type <= 0):
							flag = 0
							for i in range(1, 5):
								for m_classroom in m_classrooms:
									#这里用列表简化了字典检索，所以index为i - 1
									if (not classrooms_occupy_list[m_classroom][time_tmp][i - 1]):
										flag = 1
										classrooms_occupy_list[m_classroom][time_tmp][i - 1] = 1
										time_tmp_timetable['教室'] = m_classroom
										time_tmp_timetable['节次'] = i
										break
								if (flag):
									break
							#没有一间能用的教室
							if (not flag):
								time_tmp = time_next_day(time_tmp)
								continue
						elif (m_course.c_class_quantum_type == 1):
							flag = 0
							if (flag_noon == 0):
								for i in (1, 3):
									for m_classroom in m_classrooms:
										if ((not classrooms_occupy_list[m_classroom][time_tmp][i - 1]) and \
											(not classrooms_occupy_list[m_classroom][time_tmp][i])):
											flag = 1
											classrooms_occupy_list[m_classroom][time_tmp][i - 1] = 1
											classrooms_occupy_list[m_classroom][time_tmp][i] = 1
											time_tmp_timetable['教室'] = m_classroom
											time_tmp_timetable['节次'] = [i, i + 1]
											break
									if (flag):
										break
							elif (flag_noon == 1):
								for m_classroom in m_classrooms:
									if ((not classrooms_occupy_list[m_classroom][time_tmp][2]) and \
										(not classrooms_occupy_list[m_classroom][time_tmp][3])):
										flag = 1
										classrooms_occupy_list[m_classroom][time_tmp][2] = 1
										classrooms_occupy_list[m_classroom][time_tmp][3] = 1
										time_tmp_timetable['教室'] = m_classroom
										time_tmp_timetable['节次'] = [3, 4]
										break
							else:
								for m_classroom in m_classrooms:
									if ((not classrooms_occupy_list[m_classroom][time_tmp][0]) and \
										(not classrooms_occupy_list[m_classroom][time_tmp][1])):
										flag = 1
										classrooms_occupy_list[m_classroom][time_tmp][2] = 1
										classrooms_occupy_list[m_classroom][time_tmp][3] = 1
										time_tmp_timetable['教室'] = m_classroom
										time_tmp_timetable['节次'] = [1, 2]
										break
							if (not flag):
								time_tmp = time_next_day(time_tmp)
								continue
						else:
							flag = 0
							for m_classroom in m_classrooms:
								#这里用列表简化了字典检索，所以index为i - 1
								if ((not classrooms_occupy_list[m_classroom][time_tmp][0]) and \
									(not classrooms_occupy_list[m_classroom][time_tmp][1]) and \
									(not classrooms_occupy_list[m_classroom][time_tmp][2]) and \
									(not classrooms_occupy_list[m_classroom][time_tmp][3])):
									flag = 1
									classrooms_occupy_list[m_classroom][time_tmp][0] = 1
									classrooms_occupy_list[m_classroom][time_tmp][1] = 1
									classrooms_occupy_list[m_classroom][time_tmp][2] = 1
									classrooms_occupy_list[m_classroom][time_tmp][3] = 1
									time_tmp_timetable['教室'] = m_classroom
									time_tmp_timetable['节次'] = [1, 2, 3, 4]
									break
							#没有一间能用的教室
							if (not flag):
								time_tmp = time_next_day(time_tmp)
								continue
					else:
						time_tmp_timetable['教室'] = m_course.c_classroom
						#军事课节次在教师处确定
					#print('OK2')
					#pdb.set_trace()

					#3 处理教师约束
					if (m_course.c_class_quantum_type <= 0):
						if (m_course.c_class_type != military_sport_class):
							flag = 0
							for m_teacher in m_teachers:
								#这里用列表简化了字典检索，所以index为i - 1
								if (m_teacher.t_class_name == m_course.c_name and \
									(not teachers_occupy_list[m_teacher.t_name][time_tmp][time_tmp_timetable['节次'] - 1])):
									flag = 1
									teachers_occupy_list[m_teacher.t_name][time_tmp][time_tmp_timetable['节次'] - 1] = 1
									time_tmp_timetable['教师'] = m_teacher.t_name
									break
							#没有一个老师能上这门课
							if (not flag):
								time_tmp = time_next_day(time_tmp)
								continue
						else:
							flag = 0
							for m_teacher in m_teachers:
								#先检查最后一节课是否被占用
								if (m_teacher.t_class_name == m_course.c_name and \
									(not teachers_occupy_list[m_teacher.t_name][time_tmp][3])):
									flag = 1
									teachers_occupy_list[m_teacher.t_name][time_tmp][3] = 1
									time_tmp_timetable['教师'] = m_teacher.t_name
									time_tmp_timetable['节次'] = 4
									break
							'''
							#没有一个老师能上最后一节课,解除约束
							if (not flag):
								#最后一节课已经遍历
								for i in range(1, 4):
									for m_teacher in m_teachers:
										#这里用列表简化了字典检索，所以index为i - 1
										if (m_teacher.t_class_name == m_course.c_name and \
											(not teachers_occupy_list[m_teacher.t_name][time_tmp][i - 1])):
											flag = 1
											teachers_occupy_list[m_teacher.t_name][time_tmp][i - 1] = 1
											time_tmp_timetable['教师'] = m_teacher.t_name
											time_tmp_timetable['节次'] = i
											break
									if (flag):
										break
							'''
						#当天没有一个老师能上这门课
						if (not flag):
							time_tmp = time_next_day(time_tmp)
							continue

					elif (m_course.c_class_quantum_type == 1):
						flag = 0
						if (m_course.c_class_type == military_sport_class):
							if (flag_noon == 0):
								for i in (1, 3):
									for m_teacher in m_teachers:
										if (m_teacher.t_class_name == m_course.c_name and \
											(not teachers_occupy_list[m_teacher.t_name][time_tmp][i - 1]) and \
											(not teachers_occupy_list[m_teacher.t_name][time_tmp][i])):
											flag = 1
											teachers_occupy_list[m_teacher.t_name][time_tmp][i - 1] = 1
											teachers_occupy_list[m_teacher.t_name][time_tmp][i] = 1
											time_tmp_timetable['教师'] = m_teacher.t_name
											if (m_course.c_class_type == military_sport_class):
												time_tmp_timetable['节次'] = [i, i + 1]
											break
									if (flag):
										break
							elif (flag_noon == 1):
								for m_teacher in m_teachers:
									if (m_teacher.t_class_name == m_course.c_name and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][2]) and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][3])):
										flag = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][2] = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][3] = 1
										time_tmp_timetable['教师'] = m_teacher.t_name
										if (m_course.c_class_type == military_sport_class):
											time_tmp_timetable['节次'] = [3, 4]
										break
							else:
								for m_teacher in m_teachers:
									if (m_teacher.t_class_name == m_course.c_name and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][0]) and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][1])):
										flag = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][0] = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][1] = 1
										time_tmp_timetable['教师'] = m_teacher.t_name
										if (m_course.c_class_type == military_sport_class):
											time_tmp_timetable['节次'] = [1, 2]
										break
						else:
							for m_teacher in m_teachers:
								if (time_tmp_timetable['节次'] == [1, 2]):
									if (m_teacher.t_class_name == m_course.c_name and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][0]) and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][1])):
										flag = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][0] = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][1] = 1
										time_tmp_timetable['教师'] = m_teacher.t_name
										break
								else:
									if (m_teacher.t_class_name == m_course.c_name and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][2]) and \
										(not teachers_occupy_list[m_teacher.t_name][time_tmp][3])):
										flag = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][2] = 1
										teachers_occupy_list[m_teacher.t_name][time_tmp][3] = 1
										time_tmp_timetable['教师'] = m_teacher.t_name
										break

						if (not flag):
							time_tmp = time_next_day(time_tmp)
							continue
					else:
						flag = 0
						for m_teacher in m_teachers:
							#这里用列表简化了字典检索，所以index为i - 1
							if (m_teacher.t_class_name == m_course.c_name and \
								(not teachers_occupy_list[m_teacher.t_name][time_tmp][0]) and \
								(not teachers_occupy_list[m_teacher.t_name][time_tmp][1]) and \
								(not teachers_occupy_list[m_teacher.t_name][time_tmp][2]) and \
								(not teachers_occupy_list[m_teacher.t_name][time_tmp][3])):
								flag = 1
								time_tmp_timetable['教师'] = m_teacher.t_name
								teachers_occupy_list[m_teacher.t_name][time_tmp][0] = 1
								teachers_occupy_list[m_teacher.t_name][time_tmp][1] = 1
								teachers_occupy_list[m_teacher.t_name][time_tmp][2] = 1
								teachers_occupy_list[m_teacher.t_name][time_tmp][3] = 1
								if (m_course.c_class_type == military_sport_class):
									time_tmp_timetable['节次'] = [1, 2, 3, 4]
								break
						#没有一个老师能上这门课
						if (not flag):
							time_tmp = time_next_day(time_tmp)
							continue
					#print('OK3')
					#pdb.set_trace()
					
					#软约束的设计
					#4 当天上完课后，当天和下一天不宜安排相同的课
					#当天重复排课的情况利用continue语句,由于大循环为课程列表，小循环遍历日期，当天排完课后不会再在当天排课
					flag = 0
					if (time_tmp > start_time):
						for i in range(1, 5):
							if (m_course.c_name == timetable_all[m_teaching_class][time_before_day(time_tmp)][i]['课程名']):
								flag = 1
								break
					if (flag):
						time_tmp = time_next_day(time_tmp)
						continue
					
					#5 非连堂课相关：课时数已达到6、文化课不连堂不能够放到最后一节
					if (m_course.c_class_type > 1 and m_course.c_class_quantum_type <= 0):
						#文化课排到了最后一节，取消之
						if (day_class_hours_committed(timetable_all[m_teaching_class][time_tmp]) >= 3 or\
						 time_tmp_timetable['节次'] == 4):
							time_tmp = time_next_day(time_tmp)
							continue
					elif (m_course.c_class_type > 1 and m_course.c_class_quantum_type == 1):
						if (day_class_hours_committed(timetable_all[m_teaching_class][time_tmp]) >= 2):
							time_tmp = time_next_day(time_tmp)
							continue
					#6 连堂军事课应当安排自习休整
					elif (m_course.c_class_type <= 1 and m_course.c_class_quantum_type >= 1 and 
						day_class_hours_committed(timetable_all[m_teaching_class][time_tmp]) >= 1):
						time_tmp = time_next_day(time_tmp)
						continue
					#7 每周课程应该尽量均匀，不要相差太多
					if (week_class_hours_committed(timetable_all[m_teaching_class], time_tmp) > \
						average_class_hours_per_week(m_courses, sum_of_days(start_time, end_time, start_day)) + 2):
						time_tmp = time_next_day(time_tmp)
						continue

					#8 每周文化课不要超过4门
					#先打出课表再处理这里 
					#9 每天课程应该尽量均匀
					#先打出课表再处理这里
					#10 最后一周不排课
					#先打出课表再处理这里
					#
					#commit
					#print('OK')
					if (time_tmp_timetable['课程名'] != 0 and time_tmp_timetable['教室'] != 0 and time_tmp_timetable['教师']!= 0):
						tmp_copy = copy.deepcopy(time_tmp_timetable)
						if (m_course.c_class_quantum_type == 0):
							i = tmp_copy['节次']
							timetable_all[m_teaching_class][time_tmp][i]['课程名'] = tmp_copy['课程名']
							timetable_all[m_teaching_class][time_tmp][i]['教师'] = tmp_copy['教师']
							timetable_all[m_teaching_class][time_tmp][i]['教室'] = tmp_copy['教室']
							class_hours_tmp = class_hours_tmp - 2
						else:
							for i in tmp_copy['节次']:
								timetable_all[m_teaching_class][time_tmp][i]['课程名'] = tmp_copy['课程名']
								timetable_all[m_teaching_class][time_tmp][i]['教师'] = tmp_copy['教师']
								timetable_all[m_teaching_class][time_tmp][i]['教室'] = tmp_copy['教室']
							class_hours_tmp = class_hours_tmp - 2 * len(tmp_copy['节次'])
						del tmp_copy

					#print(time_tmp)
					#print(time_tmp_timetable['课程名'])
					#print(time_tmp_timetable['教师'])
					#print(time_tmp_timetable['教室'])
					#print(time_tmp_timetable['节次'])

					time_tmp_timetable['课程名'] = 0
					time_tmp_timetable['教师'] = 0
					time_tmp_timetable['教室'] = 0
					time_tmp_timetable['节次'] = 0
					time_tmp = time_next_day(time_tmp)
					#print('OK4')
					#pdb.set_trace()

	timetable_output = {}
	for m_teaching_class in m_teaching_classes:
		time_tmp = start_time
		tp = []
		while(time_tmp <= end_time):
			tp_tp = []
			for i in range(1, 5):
				ptr = timetable_all[m_teaching_class][time_tmp][i]['课程名']
				if (ptr == 0):
					ptr = ''
				tp_tp.append(ptr)
				del ptr
			tp.append(copy.deepcopy(tp_tp))
			del tp_tp
			time_tmp = time_next_day(time_tmp)
		timetable_output[m_teaching_class] = copy.deepcopy(tp)
		del tp

	return timetable_output

'''
#测试模块
start_time = 20190812
end_time = 20200117
start_day = 1

teachers = []
teaching_classes = ['计科', '软工', '物联网']
classrooms = ['301101', '301102', '301103', '301201', '301202', '301203', '301301', '301302', '301303', '302101', \
'302102', '302103', '302201', '302202', '302203', '302301', '302302', '302203']
courses = []

c0 = course('地形学', 24, culture_class, free, [0,0,0,0], 20191009, 20200110, ['计科', '软工', '物联网'], '室内')
c1 = course('体育三', 20, military_sport_class, free, [0,0,0,0], 20191112, 20200110, ['计科', '软工', '物联网'], '障碍场')
c2 = course('体系结构', 32, culture_class, free, [0,0,0,0], 20190902, 20191031, ['计科'], '室内')
c3 = course('操作系统', 48, culture_class, free, [0,0,0,0], 20191129, 20200110, ['计科', '物联网'], '室内')
c4 = course('数据库系统', 48, culture_class, free, [0,0,0,0], 20191127, 20200110, ['计科'], '室内')
c5 = course('野战生存', 8, culture_class, free, [0,0,0,0], 20191008, 20191101, ['计科', '软工', '物联网'], '室内')
c6 = course('软工', 64, culture_class, free, [0,0,0,0], 20190828, 20200110, ['计科', '物联网'], '室内')
c7 = course('人工智能', 64, culture_class, free, [0,0,0,0], 20190812, 20200110, ['计科'], '室内')
c8 = course('机器学习', 48, culture_class, free, [0,0,0,0], 20190829, 20200110, ['计科', '软工'], '室内')
c9 = course('毛泽东思想', 80, culture_class, free, [0,0,0,0], 20190815, 20200110, ['计科', '软工', '物联网'], '室内')
c10 = course('系统综合', 40, culture_class, two_class_hour_continuous, [0,0,0,0], 20190827, 20200110, ['计科', '物联网'], '室内')
c11 = course('数据分析', 48, culture_class, free, [0,0,0,0], 20190902, 20200110, ['计科', '软工', '物联网'], '障碍场')
c12 = course('软工', 64, culture_class, free, [0,0,0,0], 20190812, 20200110, ['软工'], '室内')
c13 = course('程序综合', 40, culture_class, free, [0,0,0,0], 20190812, 20200110, ['软工'], '室内')
c14 = course('无线通信', 64, culture_class, free, [0,0,0,0], 20190826, 20200110, ['计科', '软工', '物联网'], '室内')
c15 = course('体育达标考核', 0, major_activities, free, [1,1,1,1], 20191112, 20191112, ['计科', '软工', '物联网'], '田径场') 
c16 = course('军事地形学', 24, military_sport_class, all_day_continuous, [0,0,0,0], 20191118, 20191130, ['计科', '软工', '物联网'], '训练基地')
c16 = course('野战生存', 24, military_sport_class, all_day_continuous, [0,0,0,0], 20191105, 20191230, ['计科', '软工', '物联网'], '训练基地')
c17 = course('体检', 0, major_activities, free, [1,1,0,0], 20190903, 20190903, ['计科'], '室内')
c18 = course('体检', 0, major_activities, free, [1,1,0,0], 20190904, 20190904, ['软工'], '室内')
c19 = course('体检', 0, major_activities, free, [1,1,0,0], 20190905, 20190905, ['软工'], '室内')
c20 = course('国庆', 0, major_activities, free, [1,1,1,1], 20191001, 20191007, ['计科', '软工', '物联网'], '室内')

courses.append(c0)
courses.append(c1)
courses.append(c2)
courses.append(c3)
courses.append(c4)
courses.append(c5)
courses.append(c6)
courses.append(c7)
courses.append(c8)
courses.append(c9)
courses.append(c10)
courses.append(c11)
courses.append(c12)
courses.append(c13)
courses.append(c14)
courses.append(c15)
courses.append(c16)
courses.append(c17)
courses.append(c18)
courses.append(c19)
courses.append(c20)

t1 = teacher('刘晓才','地形学')
t2 = teacher('王叶琼','体育三')
t3 = teacher('肖舟','体育三')
t4 = teacher('沈立','体系结构')
t5 = teacher('王志英','体系结构')
t6 = teacher('罗宇','操作系统')
t7 = teacher('刘江潮','操作系统')
t8 = teacher('汪昌健','数据库系统')
t9 = teacher('刘卫东','野战生存')
t10= teacher('易光湘','野战生存')
t11= teacher('董威','软工')
t12= teacher('刘新旺','机器学习')
t13= teacher('杜雁芸','毛泽东思想')
t14= teacher('张远军','毛泽东思想')
t15= teacher('邹小军','毛泽东思想')
t16= teacher('王挺','人工智能')
t17= teacher('祝恩','人工智能')
t18= teacher('陆洪毅','系统综合')
t19= teacher('陈颖文','数据分析')
t20= teacher('黄圣春','通信原理')
t21= teacher('文艳军','操作系统')
t22= teacher('毛新军','软工')
t23= teacher('尹良泽','软工')
t24= teacher('徐建军','程序综合')
t25= teacher('逄德明','无线通信')
t26= teacher('刘晓才','地形学')
t27= teacher('刘卫东','野战生存')
t28= teacher('易光湘','野战生存')

teachers.append(t1)
teachers.append(t2)
teachers.append(t3)
teachers.append(t4)
teachers.append(t5)
teachers.append(t6)
teachers.append(t7)
teachers.append(t8)
teachers.append(t9)
teachers.append(t10)
teachers.append(t11)
teachers.append(t12)
teachers.append(t13)
teachers.append(t14)
teachers.append(t15)
teachers.append(t16)
teachers.append(t17)
teachers.append(t18)
teachers.append(t19)
teachers.append(t20)
teachers.append(t21)
teachers.append(t22)
teachers.append(t24)
teachers.append(t25)
teachers.append(t26)
teachers.append(t27)
teachers.append(t28)

x = all_information_timetable(start_time, end_time, start_day, teachers, teaching_classes, classrooms, courses)

print(x)
'''
'''
start_time = 20190812
end_time = 20200117
start_day = 1
teacher0 = ['王挺', '刘晓才', '刘新旺', '张远军', '陆洪毅', '董威', '刘卫东']
cname = ['人工智能', '军事地形学', '机器学习', '毛概', '系统综合', '软件工程', '野战生存']
major = ['计算机科学与技术', '计算机科学与技术', '计算机科学与技术', '计算机科学与技术', '计算机科学与技术', '计算机科学与技术', '计算机科学与技术']
hours = [64, 24, 48, 80, 40, 64, 24]
type0 = [2, 1, 2, 2, 2, 2, 1]
single = [0, 1, 0, 0, 1, 0, 1]
cstart = [20190812, 20191118, 20190829, 20190815, 20190823, 20190828, 20191105]
cend = [20191028, 20191125, 20191110, 20191224, 20200117, 20191025, 20191107]
cmajor = [['计算机科学与技术'], ['计算机科学与技术'], ['计算机科学与技术'], ['计算机科学与技术'], ['计算机科学与技术'], ['计算机科学与技术'], ['计算机科学与技术']]
cplace = ['室内', '田径场', '室内', '室内', '室内', '室内', '田径场']
a = cal(start_time,end_time,start_day,teacher0,cname,major,hours,type0,single,cstart,cend,cmajor,cplace)
print(a)
'''