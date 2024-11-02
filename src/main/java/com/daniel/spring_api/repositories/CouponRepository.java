package com.daniel.spring_api.repositories;

import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;

import com.daniel.spring_api.domain.coupon.Coupon;

public interface CouponRepository extends JpaRepository<Coupon, UUID>{

    
}