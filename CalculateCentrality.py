import cypher
import sys


class Centrality():
    def DegreeCentrality(self):
        print("DOGUM GUNU DEGREE CENTRALITY")
        resultsDogumDegree = cypher.run("MATCH (n:User)-[r:DOGUMGUNU]-(m:User) return n.name,n.uID,n.departmanName,count(r) as DegreeScore order by DegreeScore desc")
        print(resultsDogumDegree)
        print("TESEKKUR DEGREE CENTRALITY")
        resultsTesekkurDegree = cypher.run("MATCH (n:User)-[r:TESEKKUR]-(m:User) return n.name,n.uID,n.departmanName,count(r) as DegreeScore order by DegreeScore desc")
        print(resultsTesekkurDegree)
        print("TAKDIR DEGREE CENTRALITY")
        resultsTakdirDegree = cypher.run("MATCH (n:User)-[r:TAKDIR]-(m:User) return n.name,n.uID,n.departmanName,count(r) as DegreeScore order by DegreeScore desc")
        print(resultsTakdirDegree)


    def BetweennessCentrality(self):
        print("DOGUM GUNU BETWEENNESS CENTRALITY")
        resultsDogumBetween = cypher.run(
        "MATCH p=allShortestPaths((source:User)-[:DOGUMGUNU*]-(target:User)) UNWIND nodes(p)[1..-1] as n RETURN id(n), count(*) as betweenness order by betweenness desc")
        print(resultsDogumBetween)
        print("TESEKKUR BETWEENNESS CENTRALITY")
        resultsTesekkurBetween = cypher.run(
        "MATCH p=allShortestPaths((source:User)-[:TESEKKUR*]-(target:User)) UNWIND nodes(p)[1..-1] as n RETURN id(n), count(*) as betweenness order by betweenness desc")
        print(resultsTesekkurBetween)
        print("TAKDIR BETWEENNESS CENTRALITY")
        resultsTakdirBetween = cypher.run(
        "MATCH p=allShortestPaths((source:User)-[:TAKDIR*]-(target:User)) UNWIND nodes(p)[1..-1] as n RETURN id(n), count(*) as betweenness order by betweenness desc")
        print(resultsTakdirBetween)


    def ClosenessCentrality(self):
         print("DOGUM GUNU CLOSENESS CENTRALITY")
         resultsDogumClose = cypher.run(
        "MATCH (a:User), (b:User) WHERE a<>b WITH length(shortestPath((a)-[:DOGUMGUNU*]-(b))) AS dist, a, b RETURN DISTINCT  id(a), sum(1.0/dist) AS closenessCentrality ORDER BY closenessCentrality DESC")
         print(resultsDogumClose)
         print("TESEKKUR CLOSENESS CENTRALITY")
         resultsTesekkurClose = cypher.run(
        "MATCH (a:User), (b:User) WHERE a<>b WITH length(shortestPath((a)-[:TESEKKUR*]-(b))) AS dist, a, b RETURN DISTINCT  id(a), sum(1.0/dist) AS closenessCentrality ORDER BY closenessCentrality DESC")
         print(resultsTesekkurClose)
         print("TAKDIR CLOSENESS CENTRALITY")
         resultsTakdirClose = cypher.run(
        "MATCH (a:User), (b:User) WHERE a<>b WITH length(shortestPath((a)-[:TAKDIR*]-(b))) AS dist, a, b RETURN DISTINCT  id(a), sum(1.0/dist) AS closenessCentrality ORDER BY closenessCentrality DESC")
         print(resultsTakdirClose)


    # PageRank is used
    def EigenVectorCentrality(self):
         print("DOGUM GUNU PAGERANK CENTRALITY")
         resultDogum = cypher.run(
         "UNWIND range(1,10) AS round MATCH (n:User) WHERE rand() < 0.1  MATCH (n:User)-[:DOGUMGUNU*..10]->(m:User) SET m.rank = coalesce(m.rank,0) + 1")
         resultDogumRank = cypher.run("MATCH (n:User) WHERE n.rank is not null return id(n), n.rank order by n.rank desc")
         print(resultDogumRank)
         print("TESEKKUR PAGERANK CENTRALITY")
         resultTesekkur = cypher.run(
         "UNWIND range(1,10) AS round MATCH (n:User) WHERE rand() < 0.1  MATCH (n:User)-[:TESEKKUR*..10]->(m:User) SET m.rank = coalesce(m.rank,0) + 1")
         resultTesekkurRank = cypher.run("MATCH (n:User) WHERE n.rank is not null return id(n), n.rank order by n.rank desc")
         print(resultTesekkurRank)
         print("TAKDIR PAGERANK CENTRALITY")
         resultTakdir = cypher.run(
         "UNWIND range(1,10) AS round MATCH (n:User) WHERE rand() < 0.1  MATCH (n:User)-[:TAKDIR*..10]->(m:User) SET m.rank = coalesce(m.rank,0) + 1")
         resultTakdirRank = cypher.run("MATCH (n:User) WHERE n.rank is not null return id(n), n.rank order by n.rank desc")
         print(resultTakdir)


ex=Centrality()
#sys.stdout = open('selinCentrality.txt', 'w',buffering=0)
ex.DegreeCentrality()
ex.BetweennessCentrality()
ex.ClosenessCentrality()
ex.EigenVectorCentrality()
#sys.stdout.close()
