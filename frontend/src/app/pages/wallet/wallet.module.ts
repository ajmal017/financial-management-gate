import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";

import { WalletRoutingModule } from "./wallet-routing.module";
import { WalletComponent } from "./wallet.component";
import { FormsModule } from "@angular/forms";
import { MatSelectModule } from "@angular/material/select";
import { WalletService } from "./services/wallet.service";
import { MatDialogModule } from "@angular/material/dialog";
import { DialogWallet } from './dialogs/wallet.dialog.component';
import {MatTabsModule} from '@angular/material/tabs';
import {MatTableModule} from '@angular/material/table';

@NgModule({
  declarations: [
    WalletComponent,
    DialogWallet
  ],
  imports: [
    CommonModule,
    MatSelectModule,
    MatTabsModule,
    MatTableModule,
    FormsModule,
    WalletRoutingModule,
    MatDialogModule,
  ],
  providers: [WalletService],
})
export class WalletModule {}
