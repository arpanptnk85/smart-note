import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [],
  imports: [
    CommonModule, 
    FormsModule,
    ReactiveFormsModule,
  ],
  exports: [
    CommonModule, 
    FormsModule,
    ReactiveFormsModule,
  ], // Exporting modules to be used in other modules
})
export class SharedModule { }
