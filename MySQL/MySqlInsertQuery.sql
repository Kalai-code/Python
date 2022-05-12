insert into dept values(1,'SALES');
insert into dept values(2,'MKTG');
insert into dept values(3,'IT');
insert into dept values(4,'Admin');


select * from dept;

insert into emp values(	1,'aB',2000.00,2);
insert into emp values(2,'B',2000.00,2);
insert into emp values(3,'C',1000.00,3);
insert into emp values(4,'D',2000.00,4);
insert into emp values(5,'A',1000.00,1);
insert into emp values(6,'D1',2000.00,4);
insert into emp values(7,'A1',1000.00,1);
insert into emp values(8,'D11',200.00,4);
insert into emp values(9,'A12',100.00,1);
commit;

select * from emp;

insert into projects values (1,'INTERNAL1','1200000.00');
insert into projects values (2,'EXTERNAL1','5000000.00');
insert into projects values (3,'EXTERNAL2','5000000.00');

select * from projects;

insert into EmpProjects values (1,1,1,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (2,1,2,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (3,2,1,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (4,3,1,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));

insert into EmpProjects values (5,4,3,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (6,1,3,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (7,1,3,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));
insert into EmpProjects values (8,3,2,STR_TO_DATE('21,5,2019','%d,%m,%Y'),STR_TO_DATE('21,5,2020','%d,%m,%Y'));

commit;

select * from EmpProjects;

-- Get Total SAL of empID 1, working in projects
select sum(sal)
from (
	select e.empid,e.ename,e.sal,p.projectname
	from   EmpProjects ep
		  ,projects p
		  ,emp e
	where  ep.EmpID = e.EmpID
	and    ep.ProjectID = p.ProjectID
	and    e.empid = 1 ) ;


