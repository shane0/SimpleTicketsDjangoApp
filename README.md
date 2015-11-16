# SimpleTicketsDjangoApp
simple django ticket system that emails invoices and has a monthly billing csv export, developed while working at Mercy Hospital

there is an option to add a recurring monthly bill for clients that subscribe to hosted services

this is basically an out of box django app with a few features like an itemized invoice calculation based on time and materials, and custom admin actions for email 

csv exporting works with most hospital billing interfaces

I hosted this on linux, apache, sqlite using blueprint css framework and minimal templates

The basic function was techs can create, email and export tickets/invocies in the admin interface with a few front facing views for reporting and customer review of work done

This easily provides other uses such as asset tracking, kb, basic config management db, cmdb part of documentation for ITIL, DevOps, etc.

I have expanded models for that that include more fields if needed
