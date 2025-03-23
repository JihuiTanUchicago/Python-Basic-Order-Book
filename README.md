[Ongoing] Small Exercise for Myself to Build a Order Matching Engine.

- Activity Layer: Should handle logic to receive data from exchanges(upstream service), convert data to internally used POPOs, and pass to component
- Component Layer: Business logics for order matching.
- Builder Layer: Responsible to construct Plain Old Python Objects like `Order`, `OrderBook`, `Side`, etc.
- Dao: Responsible to get and store data in some database. Abstract layer that could represent storing to CSV file or PostgresSQL.
- Accessor: Should handle logic to signal some trading strategies in another service
