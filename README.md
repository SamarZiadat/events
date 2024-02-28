# **Technical Test**

I was assigned this scenario for a recent technical test. I used Python's csv module to create my solution.

## **Scenario**

A system generates events that are stored in a file in the following format:

event type, entity name, entity id, [fields updated], timestamp

## **Example:**

INSERTED, Placement, 12, null, 2018-04-10 12:34:56.789

INSERTED, Placement, 13, null, 2018-04-10 12:43:10.123

UPDATED, Company, 123, [status, companyUrl], 2018-04-10 12:44:00.123

UPDATED, Placement, 13, [status, hoursPerDay, overtimeRate], 2018-04-10 14:52:43.699

## **Notes:**

 - event type – can be one of INSERTED, UPDATED, DELETED
 - timestamp always in yyyy-MM-dd HH:mm:ss.ms format 
 - fields updated – are the names of the fields rather than the field data
 - events may not be in timestamp order

## **Requirement**

Develop a system that takes an events file as input and supports the following operations:
Basic:
1. Get all events of a specific event type
2. Get all events affecting a particular field. For example, all events where the status changed.
Advanced:
3. Get all events that between two timestamps (inclusive)
4. Allow combinations of (1), (2) and (3). For example, all UPDATED events where status changed
between 2018-04-10 12:00:00.000 and 2018-04-10 12:00:11.500

The output can be to the console.