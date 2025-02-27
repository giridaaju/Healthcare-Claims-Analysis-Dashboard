import sqlite3
import os

def create_database(db_path="healthcare_claims.db"):

    try:
        
        if os.path.exists(db_path):
            print(f"Database already exists at {db_path}")
            return False
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor
        
        cursor.executescript('''
        -- Patients Table
        CREATE TABLE patients (
            patient_id VARCHAR(20) PRIMARY KEY,
            birth_date DATE,
            gender VARCHAR(1),
            state VARCHAR(2),
            zip_code VARCHAR(5),
            enrollment_date DATE,
            termination_date DATE NULL,
            plan_type VARCHAR(10)
        );

        -- Providers Table
        CREATE TABLE providers (
            provider_id VARCHAR(20) PRIMARY KEY,
            provider_name VARCHAR(100),
            specialty_code VARCHAR(10),
            specialty_description VARCHAR(100),
            state VARCHAR(2),
            zip_code VARCHAR(5),
            npi VARCHAR(10) NULL
        );

        -- Claims Table
        CREATE TABLE claims (
            claim_id VARCHAR(20) PRIMARY KEY,
            patient_id VARCHAR(20),
            provider_id VARCHAR(20),
            claim_date DATE,
            admission_date DATE NULL,
            discharge_date DATE NULL,
            diagnosis_code_primary VARCHAR(10),
            diagnosis_code_1 VARCHAR(10) NULL,
            diagnosis_code_2 VARCHAR(10) NULL,
            procedure_code_primary VARCHAR(10),
            procedure_code_1 VARCHAR(10) NULL,
            procedure_code_2 VARCHAR(10) NULL,
            claim_amount DECIMAL(10,2),
            paid_amount DECIMAL(10,2),
            claim_type VARCHAR(10),
            place_of_service VARCHAR(2),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
        );

        -- Create indexes to improve query performance
        CREATE INDEX idx_claims_patient ON claims(patient_id);
        CREATE INDEX idx_claims_provider ON claims(provider_id);
        CREATE INDEX idx_claims_date ON claims(claim_date);
        CREATE INDEX idx_diagnosis ON claims(diagnosis_code_primary);
        ''')
        
    
    except Exception as e:
        print(f"Error creating database: {e}")
        return False

if __name__ == "__main__":
    create_database()