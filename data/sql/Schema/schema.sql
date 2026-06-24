CREATE DATABASE healthcare_analytics;

USE healthcare_analytics;

CREATE TABLE `patients` (
  `patient_id` int NOT NULL,
  `patient_name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `insurance_provider` varchar(100) DEFAULT NULL,
  `chronic_condition` varchar(100) DEFAULT NULL,
  `registration_date` date DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `visits` (
  `visit_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `visit_date` date DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `diagnosis` varchar(100) DEFAULT NULL,
  `treatment_cost` decimal(10,2) DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`visit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `claims` (
  `claim_id` int NOT NULL,
  `visit_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `claim_amount` decimal(10,2) DEFAULT NULL,
  `approved_amount` decimal(10,2) DEFAULT NULL,
  `claim_status` varchar(50) DEFAULT NULL,
  `denial_reason` varchar(100) DEFAULT NULL,
  `days_to_settlement` int DEFAULT NULL,
  PRIMARY KEY (`claim_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `followups` (
  `followup_id` int NOT NULL,
  `visit_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `followup_date` date DEFAULT NULL,
  `missed_followup` varchar(10) DEFAULT NULL,
  `readmission_flag` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `patient_features` (
  `patient_id` int DEFAULT NULL,
  `visit_frequency` int DEFAULT NULL,
  `total_spend` decimal(12,2) DEFAULT NULL,
  `readmission_count` int DEFAULT NULL,
  `risk_score` int DEFAULT NULL,
  `patient_segment` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




