# 💸 ExpenseTrack - Serverless Expense Tracker on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow)
![API Gateway](https://img.shields.io/badge/API-Gateway-green)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-blue)
![Cognito](https://img.shields.io/badge/AWS-Cognito-red)
![CloudFront](https://img.shields.io/badge/CloudFront-CDN-purple)

A fully serverless expense management application built on AWS that allows users to securely manage personal expenses using Amazon Cognito authentication. The application leverages API Gateway, AWS Lambda, DynamoDB, S3, and CloudFront to provide a secure, scalable, and cost-effective cloud-native solution.

---

# 🚀 Project Overview

ExpenseTrack is a serverless expense management platform where users can securely authenticate using Amazon Cognito and manage their expenses through a responsive web interface.

The application follows a modern serverless architecture:

- Amazon Cognito for Authentication
- API Gateway for API Management
- AWS Lambda for Business Logic
- DynamoDB for Data Storage
- S3 for Frontend Hosting
- CloudFront for CDN and HTTPS Delivery

---

# 🏗️ Architecture

```text
User
 │
 ▼
CloudFront
 │
 ▼
Amazon S3
 │
 ▼
Amazon Cognito
 │
 ▼
API Gateway (HTTP API)
 │
 ▼
AWS Lambda
 │
 ▼
Amazon DynamoDB
```

---

## 📸 Architecture Diagram

> Insert Screenshot Here

```text
screenshots/architecture-diagram.png
```

---

# ✨ Features

## 🔐 Authentication

- User Registration
- User Login
- User Logout
- JWT Authentication
- Cognito Managed Login
- User-Specific Data Isolation

---

## 💰 Expense Management

- Add Expense
- View Expenses
- Delete Expense
- Expense Date Tracking
- Category-wise Expense Management

---

## 🏷️ Categories

### Default Categories

- Food & Dining
- Health & Medicine
- Entertainment
- Shopping
- Travel
- Bills & Utilities
- Education
- Investments
- Personal Care
- Others

### Custom Categories

- Add Custom Category
- Delete Custom Category
- User-Specific Categories

---

## 🔒 Security

- Cognito User Pool Authentication
- JWT Authorizer
- HTTPS via CloudFront
- User-Level Data Isolation
- Secure API Access

---

# ☁️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon Cognito | Authentication & Authorization |
| API Gateway HTTP API | REST API Layer |
| AWS Lambda | Backend Compute |
| Amazon DynamoDB | NoSQL Database |
| Amazon S3 | Static Website Hosting |
| Amazon CloudFront | CDN & HTTPS |
| IAM | Permissions & Security |
| CloudWatch | Monitoring & Logs |

---

# 📸 Project Screenshots

## 1. Cognito User Pool

> Insert Screenshot Here

```text
screenshots/cognito-user-pool.png
```

### Capture:

- User Pool Overview
- Region
- User Pool ID

---

## 2. Cognito App Client

> Insert Screenshot Here

```text
screenshots/cognito-app-client.png
```

### Capture:

- Client ID
- Callback URL
- Logout URL

---

## 3. Cognito Managed Login

> Insert Screenshot Here

```text
screenshots/cognito-managed-login.png
```

---

## 4. JWT Authorizer

> Insert Screenshot Here

```text
screenshots/jwt-authorizer.png
```

### Capture:

- Issuer URL
- Audience
- Identity Source

---

## 5. API Gateway Routes

> Insert Screenshot Here

```text
screenshots/api-routes.png
```

### Routes

```text
GET     /expenses
POST    /expenses
PUT     /expenses/{id}
DELETE  /expenses/{id}

GET     /categories
POST    /categories
DELETE  /categories/{name}
```

---

## 6. API Gateway Integrations

> Insert Screenshot Here

```text
screenshots/api-integrations.png
```

---

## 7. API Gateway CORS Configuration

> Insert Screenshot Here

```text
screenshots/api-cors.png
```

### Capture:

- Allowed Origins
- Allowed Headers
- Allowed Methods

---

## 8. Lambda Functions

> Insert Screenshot Here

```text
screenshots/lambda-functions.png
```

### Functions

```text
addExpense
getExpenses
updateExpense
deleteExpense

addCategory
getCategories
deleteCategory
```

---

## 9. Lambda Function Code

> Insert Screenshot Here

```text
screenshots/lambda-code.png
```

---

## 10. DynamoDB Expenses Table

> Insert Screenshot Here

```text
screenshots/dynamodb-expenses.png
```

### Capture:

```text
Partition Key = userId
Sort Key = expenseId
```

---

## 11. DynamoDB Categories Table

> Insert Screenshot Here

```text
screenshots/dynamodb-categories.png
```

### Capture:

```text
Partition Key = userId
Sort Key = categoryName
```

---

## 12. IAM Role

> Insert Screenshot Here

```text
screenshots/iam-role.png
```

### Capture:

- DynamoDB Access
- CloudWatch Access

---

## 13. S3 Bucket Hosting

> Insert Screenshot Here

```text
screenshots/s3-hosting.png
```

### Capture:

- Bucket
- index.html
- Static Hosting

---

## 14. CloudFront Distribution

> Insert Screenshot Here

```text
screenshots/cloudfront-distribution.png
```

### Capture:

- Distribution Domain
- Origin

---

## 15. Login Page

> Insert Screenshot Here

```text
screenshots/login-page.png
```

---

## 16. Dashboard

> Insert Screenshot Here

```text
screenshots/dashboard.png
```

### Capture:

- Welcome User
- Add Expense Form
- Categories

---

## 17. Add Expense

> Insert Screenshot Here

```text
screenshots/add-expense.png
```

---

## 18. Expense List

> Insert Screenshot Here

```text
screenshots/expense-list.png
```

---

## 19. Custom Categories

> Insert Screenshot Here

```text
screenshots/custom-categories.png
```

---

# 🗄️ Database Design

## Expenses Table

| Attribute | Type |
|------------|------|
| userId | String |
| expenseId | String |
| title | String |
| amount | Number |
| category | String |
| date | String |

### Primary Key

```text
PK = userId
SK = expenseId
```

---

## Categories Table

| Attribute | Type |
|------------|------|
| userId | String |
| categoryName | String |

### Primary Key

```text
PK = userId
SK = categoryName
```

---

# 🔐 Security Architecture

The application uses Amazon Cognito JWT Authentication.

```text
User Login
      │
      ▼
Amazon Cognito
      │
      ▼
JWT Token
      │
      ▼
API Gateway JWT Authorizer
      │
      ▼
AWS Lambda
      │
      ▼
Amazon DynamoDB
```

Each user only accesses records associated with their Cognito User ID (`sub` claim).

---

# 🚀 Deployment Guide

## Step 1: Create Cognito User Pool

Create a User Pool using Amazon Cognito.

---

## Step 2: Create App Client

Configure:

```text
OAuth Flow:
Implicit Grant

Scopes:
openid
email
profile
```

---

## Step 3: Create DynamoDB Tables

### Expenses

```text
Partition Key:
userId

Sort Key:
expenseId
```

### Categories

```text
Partition Key:
userId

Sort Key:
categoryName
```

---

## Step 4: Create Lambda Functions

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

---

## Step 5: Create HTTP API Gateway

Configure routes and integrations.

---

## Step 6: Configure JWT Authorizer

### Issuer

```text
https://cognito-idp.<region>.amazonaws.com/<user_pool_id>
```

### Audience

```text
<App Client ID>
```

---

## Step 7: Configure CORS

### Allowed Origin

```text
https://your-cloudfront-domain.cloudfront.net
```

### Allowed Headers

```text
authorization
content-type
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

## Step 8: Upload Frontend

Upload:

```text
index.html
```

to Amazon S3.

---

## Step 9: Create CloudFront Distribution

Set S3 Bucket as origin.

---

## Step 10: Update Frontend Configuration

```javascript
const COGNITO_DOMAIN = "";
const CLIENT_ID = "";

const REDIRECT_URI = "";
const LOGOUT_URI = "";

const API_BASE_URL = "";
```

---

# 📊 Monitoring

CloudWatch Logs are used for:

- Lambda Monitoring
- Error Debugging
- API Requests
- Runtime Logs

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- AWS Cognito
- JWT Authentication
- API Gateway HTTP APIs
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon CloudFront
- IAM
- CloudWatch
- Serverless Architecture

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
    └── login-page.png
```

---

# 👨‍💻 Author

## Shivam Ikari

Cloud & DevOps Engineer

### Connect With Me

- GitHub: https://github.com/YOUR_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---
