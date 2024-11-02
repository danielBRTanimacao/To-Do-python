package com.daniel.spring_api.repositories;

import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;

import com.daniel.spring_api.domain.event.Event;

public interface EventRepository extends JpaRepository<Event, UUID>{
    
}
