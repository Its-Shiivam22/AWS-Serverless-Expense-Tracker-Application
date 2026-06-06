# 💸 ExpenseTrack - Serverless Expense Tracker on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)
![API Gateway](https://img.shields.io/badge/API-Gateway-green)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-blue)
![Cognito](https://img.shields.io/badge/AWS-Cognito-red)
![CloudFront](https://img.shields.io/badge/CloudFront-CDN-purple)

A fully serverless expense management application built on AWS that enables users to securely manage personal expenses through Amazon Cognito authentication. The solution leverages AWS managed services to provide a secure, scalable, highly available, and cost-effective cloud-native architecture without managing any servers.

---

# 🚀 Project Overview

ExpenseTrack is a modern serverless expense management platform where users can:

- Securely register and log in using Amazon Cognito
- Add and manage personal expenses
- Create custom expense categories
- Update or delete expenses
- View expense history
- Access only their own data through JWT-based authorization

The application follows a fully serverless architecture utilizing:

- Amazon Cognito
- Amazon API Gateway (HTTP API)
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon CloudFront
- AWS IAM
- Amazon CloudWatch

---

# 🏗️ Architecture Diagram

> Insert Architecture Diagram Screenshot Here

<p align="center">
  <img src="./Screenshots/1.AWS-Architecture.png" alt="ExpenseTrack Architecture" width="1000">
</p>

```text
Screenshots/1.AWS-Architecture.png
```

---

# 🏗️ Architecture Flow

1. User accesses the application through CloudFront.
2. CloudFront serves static frontend files from Amazon S3.
3. User authenticates using Amazon Cognito.
4. Cognito generates a JWT Access Token.
5. Frontend sends requests to API Gateway.
6. API Gateway validates the JWT token using a Cognito JWT Authorizer.
7. API Gateway invokes Lambda functions.
8. Lambda performs business logic.
9. Lambda interacts with DynamoDB.
10. Response is returned to the frontend.

---

# ✨ Features

## 🔐 Authentication

- User Registration
- User Login
- User Logout
- JWT Authentication
- Cognito Hosted Login
- Secure Session Management
- User-Specific Data Isolation

## 💰 Expense Management

- Add Expenses
- View Expenses
- Update Expenses
- Delete Expenses
- Track Expense Amounts
- Track Expense Dates

## 📂 Category Management

- Create Categories
- View Categories
- Delete Categories
- Custom User Categories

## ☁️ Cloud Features

- Serverless Architecture
- Auto Scaling
- Fully Managed Services
- HTTPS Delivery
- CDN Acceleration
- High Availability

---

# 📸 Application Screenshots

## Login Page

> Insert Screenshot Here

```text
Screenshots/login-page.png
```

---

## Dashboard

> Insert Screenshot Here

```text
Screenshots/dashboard.png
```

---

## Add Expense

> Insert Screenshot Here

```text
Screenshots/add-expense.png
```

---

## Expense List

> Insert Screenshot Here

```text
Screenshots/expense-list.png
```

---

# 🔐 Authentication Architecture

Amazon Cognito is used to manage user authentication and authorization.

### Authentication Flow

1. User logs in through Cognito Hosted UI.
2. Cognito validates credentials.
3. Cognito issues JWT Access Token.
4. Frontend stores token.
5. Token is sent in Authorization header.
6. API Gateway validates JWT.
7. Authorized requests invoke Lambda functions.

---

# 🌐 API Gateway Configuration

## API Gateway Type

```text
Amazon API Gateway HTTP API
```

HTTP APIs were selected because they provide:

- Lower Cost
- Lower Latency
- Native JWT Authorizer Support
- Simplified Configuration

---

## API Routes

> Insert Screenshot Here

```text
Screenshots/api-routes.png
```

### Expense Routes

```text
GET     /expenses
POST    /expenses
PUT     /expenses/{id}
DELETE  /expenses/{id}
```

### Category Routes

```text
GET     /categories
POST    /categories
DELETE  /categories/{name}
```

---

# ⚙️ Lambda Functions

> Insert Screenshot Here

```text
Screenshots/lambda-functions.png
```

### Expense Functions

```text
addExpense
getExpenses
updateExpense
deleteExpense
```

### Category Functions

```text
addCategory
getCategories
deleteCategory
```

---

# 🗄️ Database Design

Amazon DynamoDB is used as the application's NoSQL database.

---

## Expenses Table

### Primary Key

```text
PK = userId
SK = expenseId
```

### Example Record

```json
{
  "userId": "12345",
  "expenseId": "exp001",
  "amount": 500,
  "category": "Food",
  "description": "Lunch",
  "date": "2026-06-01"
}
```

---

## Categories Table

### Primary Key

```text
PK = userId
SK = categoryName
```

### Example Record

```json
{
  "userId": "12345",
  "categoryName": "Food"
}
```

---

## Data Isolation

Each user's data is isolated using:

```text
Cognito User ID (sub claim)
```

Users can only access records belonging to their own account.

---

# 🔒 Security

The application follows AWS security best practices.

### Security Controls

- Amazon Cognito Authentication
- JWT Validation via API Gateway
- HTTPS via CloudFront
- User-Level Data Isolation
- IAM Least Privilege Access
- No Hardcoded Credentials
- Secure Backend APIs
- Private DynamoDB Access through Lambda

---

# 🚀 Deployment Guide

## Step 1 — Create Cognito User Pool

Create an Amazon Cognito User Pool.

> Insert Screenshot Here

```text
Screenshots/cognito-user-pool.png
```

---

## Step 2 — Create App Client

Configure:

```text
OAuth Flow:
Authorization Code Grant

Scopes:
openid
email
profile
```

> Insert Screenshot Here

```text
Screenshots/cognito-app-client.png
```

---

## Step 3 — Create DynamoDB Tables

### Expenses Table

```text
Partition Key:
userId

Sort Key:
expenseId
```

### Categories Table

```text
Partition Key:
userId

Sort Key:
categoryName
```

> Insert Screenshot Here

```text
Screenshots/dynamodb-expenses.png
```

```text
Screenshots/dynamodb-categories.png
```

---

## Step 4 — Create Lambda Functions

Create:

```text
addExpense
getExpenses
updateExpense
deleteExpense

addCategory
getCategories
deleteCategory
```

Assign IAM permissions for DynamoDB access.

---

## Step 5 — Create HTTP API Gateway

Configure routes and Lambda integrations.

> Insert Screenshot Here

```text
Screenshots/api-integrations.png
```

---

## Step 6 — Configure JWT Authorizer

### Issuer

```text
https://cognito-idp.<region>.amazonaws.com/<user_pool_id>
```

### Audience

```text
<App Client ID>
```

> Insert Screenshot Here

```text
Screenshots/jwt-authorizer.png
```

---

## Step 7 — Configure CORS

### Allowed Origins

```text
https://your-cloudfront-domain.cloudfront.net
```

### Allowed Headers

```text
authorization
content-type
x-amz-date
x-api-key
x-amz-security-token
```

### Allowed Methods

```text
GET
POST
PUT
DELETE
OPTIONS
```

---

## Step 8 — Upload Frontend to S3

Upload:

```text
index.html
```

Enable Static Website Hosting.

---

## Step 9 — Create CloudFront Distribution

Use the S3 bucket as origin.

> Insert Screenshot Here

```text
Screenshots/cloudfront-distribution.png
```

---

## Step 10 — Update Frontend Configuration

Replace values in:

```javascript
const COGNITO_DOMAIN = "";
const CLIENT_ID = "";

const REDIRECT_URI = "";
const LOGOUT_URI = "";

const API_BASE_URL = "";
```

---

# 📊 Monitoring & Logging

Amazon CloudWatch is used for:

- Lambda Logs
- Runtime Errors
- API Debugging
- Request Tracking
- Performance Monitoring

Benefits:

- Centralized Logging
- Error Troubleshooting
- Operational Visibility

---

# 💰 Cost Optimization

This project was designed with cost efficiency in mind.

### Cost Saving Services

- AWS Lambda (Pay-per-use)
- DynamoDB On-Demand
- API Gateway HTTP API
- Amazon S3
- CloudFront

### Benefits

- No EC2 Servers
- No Load Balancers
- No Database Administration
- No Infrastructure Maintenance

This architecture significantly reduces operational costs while remaining highly scalable.

---

# 🛠️ Challenges Faced

## JWT Authentication

### Challenge

Configuring Cognito authentication with API Gateway.

### Solution

Configured API Gateway JWT Authorizer using Cognito User Pool Issuer URL and App Client ID.

---

## CORS Configuration

### Challenge

Frontend requests blocked by browser CORS policies.

### Solution

Configured HTTP API CORS settings and Lambda response headers.

---

## User Data Isolation

### Challenge

Preventing users from viewing each other's expenses.

### Solution

Used Cognito User ID (`sub`) as DynamoDB partition key.

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Amazon Cognito
- JWT Authentication
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon CloudFront
- AWS IAM
- Amazon CloudWatch
- Serverless Architecture
- Security Best Practices
- Event-Driven Computing
- Cloud-Native Application Development

---

# 🚀 Future Enhancements

Planned improvements include:

- Expense Analytics Dashboard
- Monthly Expense Reports
- Budget Tracking
- CSV Export
- PDF Reports
- Email Notifications
- Search Functionality
- Expense Filters
- Multi-Currency Support
- Infrastructure as Code (Terraform)
- CI/CD Pipeline with GitHub Actions

---

# 📂 Repository Structure

```text
ExpenseTrack/
│
├── index.html
├── README.md
│
├── lambda/
│   ├── addExpense.py
│   ├── getExpenses.py
│   ├── updateExpense.py
│   ├── deleteExpense.py
│   ├── addCategory.py
│   ├── getCategories.py
│   └── deleteCategory.py
│
├── architecture/
│   └── architecture-diagram.png
│
└── screenshots/
    ├── cognito-user-pool.png
    ├── cognito-app-client.png
    ├── jwt-authorizer.png
    ├── api-routes.png
    ├── api-integrations.png
    ├── dynamodb-expenses.png
    ├── dynamodb-categories.png
    ├── cloudfront-distribution.png
    ├── dashboard.png
    ├── login-page.png
    ├── add-expense.png
    └── expense-list.png
```

---

# 👨‍💻 Author

## Shivam Ikari

AWS Certified Solutions Architect – Associate

Cloud & DevOps Engineer

### Connect With Me

- GitHub: https://github.com/Shiivam22
- LinkedIn: https://www.linkedin.com/in/shivam-ikari
- Email: shivamekale07@gmail.com

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---

## 📜 License

This project is intended for educational and portfolio purposes.

Feel free to fork, learn, and build upon it.
