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

## 📸 Architecture Diagram

<p align="center">
  <img src="./Screenshots/1.AWS-Architecture.png" alt="ExpenseTrack Architecture" width="1000">
</p>

```text
/Screenshots/1.AWS-Architecture.png
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


## API Gateway Routes

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

## Lambda Functions

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

# 🗄️ Database Design

## Expenses Table
```text
PK = userId
SK = expenseId
```

## Categories Table
```text
PK = userId
SK = categoryName
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
