## API Documentation

#### Index
- URL: `/`
- Method: GET
- Description: Renders the index page of the application.

#### Organization List
- URL: `/organizations/`
- Method: GET
- Description: Retrieves a list of organizations.

#### Organization Number
- URL: `/organizations/number/`
- Method: GET
- Description: Retrieves the count of organizations.

#### Organization Detail
- URL: `/organizations/<int:pk>/`
- Method: GET
- Description: Retrieves details of a specific organization identified by its primary key (`pk`).

#### Add Organization
- URL: `/organizations/add/`
- Method: GET, POST
- Description: Renders a form to add a new organization. Accepts form submission to create a new organization.

#### Edit Organization
- URL: `/organizations/<int:pk>/edit/`
- Method: GET, POST
- Description: Renders a form to edit an existing organization identified by its primary key (`pk`). Accepts form submission to update the organization.

#### Delete Organization
- URL: `/organizations/<int:pk>/delete/`
- Method: POST
- Description: Deletes an existing organization identified by its primary key (`pk`).

#### Organizations Socials
- URL: `/organizations/socials/`
- Method: GET
- Description: Retrieves a list of organizations and their socials.

#### Edit Socials
- URL: `/organizations/socials/<int:organization_id>/edit/`
- Method: GET, POST
- Description: Renders a form to edit the socials of a specific organization identified by its ID (`organization_id`). Accepts form submission to update the socials.

#### Organization Names
URL: `/organization-names/`
Method: GET
Description: Retrieves a list of organization names.

#### Organization Leaders
- URL: `/organization-leaders/<int:organization_id>/`
- Method: GET
- Description: Retrieves a list of leaders for a specific organization identified by its ID (`organization_id`).

#### Edit Leader
- URL: `/organization-leaders/<int:organization_id>/<int:leader_id>/edit/`
- Method: GET, POST
- Description: Renders a form to edit an existing leader of a specific organization identified by its ID (`organization_id`) and leader ID (`leader_id`). Accepts form submission to update the leader.

#### Delete Leader
- URL: `/organization-leaders/<int:organization_id>/<int:leader_id>/delete/`
- Method: POST
- Description: Deletes an existing leader of a specific organization identified by its ID (`organization_id`) and leader ID (`leader_id`).

#### Add Leader
- URL: `/organization-leaders/<int:organization_id>/add/`
- Method: GET, POST
- Description: Renders a form to add a new leader to a specific organization identified by its ID (`organization_id`). Accepts form submission to create a new leader.

#### Organizations Contacts
- URL: `/organizations-contacts/`
- Method: GET
- Description: Retrieves a list of organizations and their contacts.

#### Add Contact
- URL: `/organizations-contacts/<int:organization_id>/add/`
- Method: GET, POST
- Description: Renders a form to add a new contact to a specific organization identified by its ID (`organization_id`). Accepts form submission to create a new contact.

#### Edit Contact
- URL: `/organizations-contacts/<int:organization_id>/edit/`
- Method: GET, POST
- Description: Renders a form to edit an existing contact of a specific organization identified by its ID (`organization_id`). Accepts form submission to update the contact.

#### Delete Contact
- URL: `/organizations-contacts/<int:organization_id>/delete/`
- Method: POST
- Description: Deletes an existing contact of a specific organization identified by its ID (`organization_id`).


