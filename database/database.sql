
CREATE DATABASE IF NOT EXISTS stock_app
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE stock_app;

CREATE TABLE IF NOT EXISTS users (
  id                CHAR(36)      NOT NULL PRIMARY KEY,  
  first_name        VARCHAR(50)   NOT NULL,
  last_name         VARCHAR(50)   NOT NULL,
  email             VARCHAR(255)  NOT NULL UNIQUE,        
  password_hash     VARCHAR(255)  NOT NULL,               
  age               INT           NOT NULL,
  country           VARCHAR(100)  NOT NULL,
  timezone          VARCHAR(64)   NOT NULL,               
  profile_image_url VARCHAR(500)  NULL,                   
  email_verified    BOOLEAN       NOT NULL DEFAULT FALSE,
  status            VARCHAR(20)   NOT NULL DEFAULT 'ACTIVE',
  created_at        DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS email_otp (
  otp_id      INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id     CHAR(36)     NOT NULL,                     
  purpose     ENUM('EMAIL_VERIFICATION', 'PASSWORD_RESET') NOT NULL,
  otp_hash    VARCHAR(255) NOT NULL,                     
  expires_at  DATETIME     NOT NULL,
  attempts    INT          NOT NULL DEFAULT 0,
  is_used     BOOLEAN      NOT NULL DEFAULT FALSE,
  created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT fk_otp_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sectors (
  sector_id    INT           NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sector_name  VARCHAR(100)  NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS user_sectors (
  user_id    CHAR(36)  NOT NULL,
  sector_id  INT       NOT NULL,

  PRIMARY KEY (user_id, sector_id),

  CONSTRAINT fk_user_sectors_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE,

  CONSTRAINT fk_user_sectors_sector
    FOREIGN KEY (sector_id) REFERENCES sectors(sector_id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_interests (
  user_id   CHAR(36)      NOT NULL,
  interest  VARCHAR(100)  NOT NULL,

  PRIMARY KEY (user_id, interest),

  CONSTRAINT fk_user_interests_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS user_preference (
  preference_id    INT           NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id          CHAR(36)      NOT NULL UNIQUE,
  investment_goal  VARCHAR(100)  NULL,

  CONSTRAINT fk_preference_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
);
