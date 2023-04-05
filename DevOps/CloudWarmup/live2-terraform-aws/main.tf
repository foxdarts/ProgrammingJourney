#first step is to specify a provider


terraform {

    required_providers {

      aws = { #which cloud provider your going to use
        
        source = "hashicorp/aws"

        version = "~> 4.16"

      }

    }

    required_version = ">= 1.2.0"
    
}

#specify provider location for server

provider "aws" {

    region = "us-east-2"

}

#resource configuration

resource "aws_s3_bucket" "s3_bucket" { #creates "first" named "second"

    bucket = "tcb-app-qa-df" #unique name for bucket

}

#make the resources within the bucket private

resource "aws_s3_bucket_public_access_block" "s3_block" {

    bucket = aws_s3_bucket.s3_bucket.id #refrence to last resource block

    block_public_acls = true
    block_public_policy = true
    ignore_public_acls = true
    restrict_public_buckets = true

}
