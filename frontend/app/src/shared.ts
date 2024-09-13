// shared.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [CommonModule, FormsModule],
  exports: [CommonModule, FormsModule], // Exporting modules to be used in other modules
})
export class SharedModule {}
