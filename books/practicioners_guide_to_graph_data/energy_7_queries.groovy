// wrap our query of valid paths in a method

def getSensorsFromTower(g, start, tower){
    sensors = g.withSack(start).V(tower).
        repeat(
            inE("send").as("sendEdge").
            where(eq("sendEdge")).
                by(sack()).
                by("timestep").
            sack(minus).
                by(constant(1)).
            outV()as("visitedVertex").
            simplePath()).
        times(start+1).
        as("endingSensor").
        select("endingSensor").
        by(values("sensor_name")).
        toList()
    
    return sensors;
}

atRiskSensors = [] as Set;
tower = g.V().has("Tower", "tower_name", "Georgetown").next()

for (time = 0; time < 6; time++){
    atRiskSensors.addAll(getSensorsFromTower(g, time, tower));
}

// note, if dont declare as set
// atRiskSensors = atRiskSensors.flatten().unique();


def getTowersFromSensor(g, start, sensor) {
    towers = g.withSack(start).V(sensor).as("startingSensor").
        until(hasLabel("Tower")).
        repeat(outE("send").as("sendEdge").
            where(eq("sendEdge")).
                by(sack()).
                by("timestep").
            inV().as("visitedVertex").
            sack(sum).
            by(constant(1))).
        as("endingTower").
        select("endingTower").
        by(values("tower_name")).
        dedup().
        tolist()

    return towers;
}

otherTowers = [:]  // create a map

for (i=0; i < atRiskSensors.size(); i++){
    otherTowers[atRiskSensors[i]] = [];
    sensor = g.V().has("Sensor", "sensor_name", atRiskSensors[i]).next()
    for(time=0; time < 6; time++){
        otherTowers[atRiskSensor[i]].add(
            getTowersFromSensor(g, time, sensor)
        );
    }

    // flatten to only unique tower names
    otherTowers[atRiskSensors[i]] = otherTowers[atRiskSensors[i]].flatten().unique();
}

