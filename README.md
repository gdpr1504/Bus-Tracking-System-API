Bus Tracking System API - 1.6
--------------------------------
Change Log : added _/busstops_(POST,DELETE,GET). added _/complaints_(POST,GET). changed timezone to IST. updated _/routes_. updated _/reports_.
--------------------------------
The Rest API has been deployed to AWS.

Link: _ec2-3-7-131-60.ap-south-1.compute.amazonaws.com_

Everybody can use the below endpoints to access the tables in the database.

* _/register_ - POST into Users table.
* _/login_ - takes a JSON object with 'username' and 'password' and gives back JWT if exists in Users table. The JWT shall be used to access all the end points. For all the endpoints an Authorization Header should be included with value 'Bearer <JWT>'.
* _/tracking_ (POST) - POST into Rawdata table.
* _/tracking_ (GET) - takes a JSON object with 'routeId' and 'deviceTime' and sends back Livedata with respect to input.
```
if 'routeId' == None and 'deviceTime' == None:
	returns Livedata of all Routes
if 'routeId' != None and 'deviceTime' == None:
	returns Livedata of given 'routeId'
if 'routeId' != None and 'deviceTime' != None:
	returns Tracking of given 'routeId' at given 'deviceTime'
```
* _/routes_ - takes a JSON object with 'routeId' and sends back Information about the routes.
```
if 'routeId' == None:
	returns Route Information of all Routes
if 'routeId' != None:
	returns Route Information of given 'routeId'
```
* _/busstops_ (POST) - POST into BusStops table.
* _/busstops_ (DELETE) - takes a JSON object with 'routeId' and 'busStopName' and deletes given BusStop if exists.
* _/busstops_ (GET) - takes a JSON object with 'routeId'.
```
if 'routeId' == None:
	returns a list of BusStops of all Routes.
if 'routeId' != None:
	returns a list of BusStops of given 'routeId'.
```
* _/geofence_ (POST) - POST into Geofence table.
* _/geofence_ (GET) - takes a JSON object with 'routeId','fromDate','toDate','status'. 'fromDate' and 'toDate' are must.
```
if 'status' == None:
	if 'routeId' == None:
		returns all geofence data of all Routes
	if 'routeId' != None:
		returns all geofence data of given 'routeId'
if 'status' != None:
	if 'routeId' == None:
		returns geofence data of all Routes with given 'status'
	if 'routeId' != None:
		returns geofence data of given 'routeId' with given 'status'
```
* _/busgeofence_ (POST) - POST into BusGeofence table.
* _/busgeofence_ (DELETE) - takes a JSON object with 'routeId' and deletes all the rows from BusGeofence table with the given 'routeId' if exists.
* _/busgeofence_ (GET) - takes a JSON object with 'routeId'.
```
if 'routeId' == None:
	returns a list of latitudes and logitudes detetrmining bus geofence of all Routes.
if 'routeId' != None:
	returns a list of latitudes and logitudes detetrmining bus geofence of given 'routeId'.
```
* _/alertscontrol_ (POST) - POST into AlertsControl Table.
* _/alertscontrol_ (DELETE) - takes a JSON object with 'alertCode' and deletes the AlertControl with the given 'alertCode' if exists.
* _/alertscontrol_ (GET) - AlertsControl Table.
* _/alerts_ (POST) - POST into Alerts table.
* _/alerts_ (GET) - takes a JSON object with 'routeId' and 'alertDate'. 'alertDate' is must.
```
if 'routeId' == None:
	returns a list of alerts generated on given 'alertDate'.
if 'routeId' != None:
	returns a list of alerts generated by given 'routeId' on given 'alertDate'.
```
* _/reports/uptime_ - takes a JSON object with 'routeId', 'fromDate', 'toDate'. 'fromDate', 'toDate' are must.
```
if 'routeId' == None:
	returns uptime data of all buses between given dates
if 'routeId' != None:
	returns uptime data of given 'routeId' between given dates
```
* _/reports/fleet_ - takes a JSON object with 'routeId', 'fromDate', 'toDate'.
```
if 'fromDate' and 'toDate' == None:
	if 'routeId' == None:
		returns all fleet data of all buses
	if 'routeId' != None:
		returns all fleet data of given 'routeId'
if 'fromDate' and 'toDate' != None:
	if 'routeId' == None:
		returns fleet data of all buses between given dates
	if 'routeId' != None:
		returns fleet data of given 'routeId' between given dates
```
* _/reports/distance_ - takes a JSON object with 'routeId', 'fromDate', 'toDate'. 'fromDate', 'toDate' are must.
```
if 'routeId' == None:
	returns distance travelled data of all buses between given dates
if 'routeId' != None:
	returns distance travelled data of given bus between given dates
```
* _/reports/alerts_ - takes a JSON object with 'alertCode', 'fromDate', 'toDate'. 'fromDate', 'toDate' are must.
```
if 'alertCode' == None:
	returns all alerts buses between given dates
if 'alertCode' != None:
	returns all alerts of given type between given dates
```
* _/complaints_ (POST)- POST into Complaints Table.
* _/complaints_ (GET)- takes a JSON object with 'cFrom', 'cDate' and returns a list of Complaints. 'cDate' is must.
```
if 'cFrom' == None:
	returns a list of all Complaints on given cDate
if 'cFrom' == 'staff':
	returns a list of Complaints on given cDate given by staff
if 'cFrom' == 'student':
	returns a list of Complaints on given cDate given by students
```
* _/sms_ - sends SMS in bulk. takes a JSON object with 'to' and 'message'.
```
if 'to' == 'users':
	given message is sent to all Users.
if 'to' == 'drivers':
	given message is sent to all Drivers.
```
* _/buses_ - Bus table.
* _/drivers_ - Driver table.
* _/sos_ - Sos table.
* _/users_ - Users table.

Example: _ec2-3-7-131-60.ap-south-1.compute.amazonaws.com/routes_

All the endpoints returns the data as a list of dictionaries in JSON format which can be converted and used in the program directly.
