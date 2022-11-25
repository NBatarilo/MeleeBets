export class Bet {
    constructor(
      public bettor_username: string,
      public odds: number,
      public amount: number,
      public outcome: number,
      public payout: number,
      public _id?: number,
      public updatedAt?: Date,
      public createdAt?: Date,
      public lastUpdatedBy?: string,
    ) { }
}