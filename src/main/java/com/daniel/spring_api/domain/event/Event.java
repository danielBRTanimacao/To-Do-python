package com.daniel.spring_api.domain.event;

import java.util.UUID;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Table(name = "event")
@Entity
public class Event {
    @Id
    @GeneratedValue
    private UUID id;

    private String title;
}
